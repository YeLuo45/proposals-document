/**
 * Manager Agent - Orchestrates multi-agent workflow and state machine
 */

import { 
  AgentType, 
  MessageType, 
  DocumentStatus, 
  DocumentEvent, 
  AgentMessage,
  MessageHandler,
  AgentResult 
} from '../../types/agent';
import { DocumentState } from '../../types/document';
import { AgentLoop, agentLoop } from '../agentLoop';
import { contextPool } from '../../store/contextPool';

/**
 * Agent registry interface
 */
interface AgentRegistry {
  dispatch(agentType: AgentType, message: AgentMessage): Promise<AgentResult>;
}

/**
 * Manager Agent configuration
 */
interface ManagerConfig {
  agentLoop: AgentLoop;
  contextPool: typeof contextPool;
  autoApproveThreshold?: number;
  maxRetries?: number;
}

export class ManagerAgent {
  private config: ManagerConfig;
  private messageBus: MessageBus | null = null;
  private running: boolean = false;
  private handlers: Map<string, MessageHandler> = new Map();

  constructor(config: Partial<ManagerConfig> = {}) {
    this.config = {
      agentLoop: config.agentLoop || agentLoop,
      contextPool: config.contextPool || contextPool,
      autoApproveThreshold: config.autoApproveThreshold ?? 0.8,
      maxRetries: config.maxRetries ?? 3
    };
  }

  /**
   * Set the message bus instance
   */
  setMessageBus(bus: MessageBus): void {
    this.messageBus = bus;
  }

  /**
   * Start listening to messages
   */
  async listen(): Promise<void> {
    if (!this.messageBus) {
      console.warn('[ManagerAgent] No messageBus set, using mock mode');
    }

    this.running = true;
    console.log('[ManagerAgent] Listening for messages');

    // Subscribe to agent loop state changes
    this.config.agentLoop.subscribeAll((state, event) => {
      this.handleStateChange(state, event);
    });
  }

  /**
   * Stop listening to messages
   */
  async stop(): Promise<void> {
    this.running = false;
    console.log('[ManagerAgent] Stopped');
  }

  /**
   * Check if manager is running
   */
  isRunning(): boolean {
    return this.running;
  }

  /**
   * Handle state change events from AgentLoop
   */
  private handleStateChange(state: DocumentState, event: DocumentEvent): void {
    console.log(`[ManagerAgent] State changed: ${state.id} - ${event}`);

    // Auto-handle based on status
    switch (state.status) {
      case DocumentStatus.IN_REVIEW:
        this.scheduleReview(state);
        break;
      case DocumentStatus.APPROVED:
        this.schedulePublish(state);
        break;
      case DocumentStatus.REJECTED:
        this.handleRejection(state);
        break;
    }
  }

  /**
   * Schedule review for a document
   */
  private scheduleReview(state: DocumentState): void {
    if (this.messageBus) {
      this.messageBus.publish({
        id: `review-${state.id}-${Date.now()}`,
        sender: AgentType.MANAGER,
        receiver: AgentType.REVIEWER,
        type: MessageType.REVIEW_REQUEST,
        payload: {
          documentId: state.id,
          content: state.content,
          title: state.title,
          conversationId: state.conversationId
        },
        timestamp: Date.now(),
        conversationId: state.conversationId
      });
    }
  }

  /**
   * Schedule publishing for an approved document
   */
  private schedulePublish(state: DocumentState): void {
    console.log(`[ManagerAgent] Document ${state.id} approved, ready for publishing`);
  }

  /**
   * Handle document rejection
   */
  private handleRejection(state: DocumentState): void {
    console.log(`[ManagerAgent] Document ${state.id} rejected, returning to draft`);
    this.transitionDocumentStatus(state.id, DocumentEvent.REVISE, { reason: 'rejected' });
  }

  /**
   * Dispatch document to appropriate agent based on status
   */
  dispatch(state: DocumentState): void {
    switch (state.status) {
      case DocumentStatus.DRAFT:
        this.dispatchToEditor(state);
        break;
      case DocumentStatus.IN_REVIEW:
        this.dispatchToReviewer(state);
        break;
      case DocumentStatus.REVISED:
        this.dispatchToResearcher(state);
        break;
      default:
        console.log(`[ManagerAgent] No dispatch needed for status: ${state.status}`);
    }
  }

  /**
   * Dispatch to Editor Agent
   */
  private dispatchToEditor(state: DocumentState): void {
    if (this.messageBus) {
      this.messageBus.publish({
        id: `edit-${state.id}-${Date.now()}`,
        sender: AgentType.MANAGER,
        receiver: AgentType.EDITOR,
        type: MessageType.EDIT_REQUEST,
        payload: {
          documentId: state.id,
          content: state.content,
          title: state.title,
          conversationId: state.conversationId
        },
        timestamp: Date.now(),
        conversationId: state.conversationId
      });
    }
  }

  /**
   * Dispatch to Reviewer Agent
   */
  private dispatchToReviewer(state: DocumentState): void {
    if (this.messageBus) {
      this.messageBus.publish({
        id: `review-${state.id}-${Date.now()}`,
        sender: AgentType.MANAGER,
        receiver: AgentType.REVIEWER,
        type: MessageType.REVIEW_REQUEST,
        payload: {
          documentId: state.id,
          content: state.content,
          title: state.title,
          conversationId: state.conversationId
        },
        timestamp: Date.now(),
        conversationId: state.conversationId
      });
    }
  }

  /**
   * Dispatch to Researcher Agent
   */
  private dispatchToResearcher(state: DocumentState): void {
    if (this.messageBus) {
      this.messageBus.publish({
        id: `research-${state.id}-${Date.now()}`,
        sender: AgentType.MANAGER,
        receiver: AgentType.RESEARCHER,
        type: MessageType.RESEARCH_REQUEST,
        payload: {
          documentId: state.id,
          content: state.content,
          title: state.title,
          conversationId: state.conversationId
        },
        timestamp: Date.now(),
        conversationId: state.conversationId
      });
    }
  }

  /**
   * Handle result from Editor Agent
   */
  async handleEditorResult(result: AgentResult, documentId: string): Promise<void> {
    console.log(`[ManagerAgent] Editor result for ${documentId}:`, result);

    if (result.success) {
      // Update content in agent loop
      if (result.data?.content) {
        this.config.agentLoop.updateContent(documentId, result.data.content);
      }

      // Save context
      this.config.contextPool.saveContext(documentId, {
        lastEditorResult: result,
        timestamp: Date.now()
      });
    } else {
      console.error(`[ManagerAgent] Editor failed for ${documentId}:`, result.error);
    }
  }

  /**
   * Handle result from Reviewer Agent
   */
  async handleReviewerResult(result: AgentResult, documentId: string): Promise<void> {
    console.log(`[ManagerAgent] Reviewer result for ${documentId}:`, result);

    const state = this.config.agentLoop.getState(documentId);
    if (!state) {
      console.warn(`[ManagerAgent] Document ${documentId} not found`);
      return;
    }

    if (result.success) {
      const score = result.score ?? 0;

      // Auto-approve if above threshold
      if (score >= this.config.autoApproveThreshold) {
        this.transitionDocumentStatus(documentId, DocumentEvent.REVIEW_PASS, { score });
      } else {
        // Needs revision
        this.transitionDocumentStatus(documentId, DocumentEvent.REVIEW_REJECT, { 
          score, 
          suggestions: result.data 
        });
      }
    } else {
      console.error(`[ManagerAgent] Reviewer failed for ${documentId}:`, result.error);
      this.transitionDocumentStatus(documentId, DocumentEvent.REVIEW_REJECT, { 
        error: result.error 
      });
    }
  }

  /**
   * Handle result from Researcher Agent
   */
  async handleResearcherResult(result: AgentResult, documentId: string): Promise<void> {
    console.log(`[ManagerAgent] Researcher result for ${documentId}:`, result);

    if (result.success) {
      // Save research context
      const existingContext = this.config.contextPool.loadContext(documentId) || {};
      this.config.contextPool.saveContext(documentId, {
        ...existingContext,
        researchResult: result.data,
        researchTimestamp: Date.now()
      });
    } else {
      console.error(`[ManagerAgent] Researcher failed for ${documentId}:`, result.error);
    }
  }

  /**
   * Transition document status using AgentLoop
   */
  transitionDocumentStatus(
    documentId: string, 
    event: DocumentEvent, 
    data?: any
  ): DocumentState | null {
    const state = this.config.agentLoop.getState(documentId);
    if (!state) {
      console.warn(`[ManagerAgent] Document ${documentId} not found`);
      return null;
    }

    const result = this.config.agentLoop.processEvent(documentId, event, data);
    
    if (result) {
      console.log(`[ManagerAgent] Transitioned ${documentId} to ${result.status}`);
      
      // Dispatch to next agent based on new status
      this.dispatch(result);
    }

    return result;
  }

  /**
   * Create and register a new document
   */
  createDocument(
    id: string, 
    title: string, 
    content: string, 
    conversationId: string
  ): DocumentState {
    const state = this.config.agentLoop.createDocument(id, title, conversationId);
    if (content) {
      this.config.agentLoop.updateContent(id, content);
    }
    return state;
  }

  /**
   * Get document state
   */
  getDocumentState(docId: string): DocumentState | undefined {
    return this.config.agentLoop.getState(docId);
  }

  /**
   * Submit document for review
   */
  submitForReview(documentId: string): DocumentState | null {
    return this.transitionDocumentStatus(documentId, DocumentEvent.SUBMIT_FOR_REVIEW);
  }

  /**
   * Save document
   */
  saveDocument(documentId: string, content: string): DocumentState | null {
    this.config.agentLoop.updateContent(documentId, content);
    return this.transitionDocumentStatus(documentId, DocumentEvent.SAVE);
  }

  /**
   * Approve document
   */
  approveDocument(documentId: string): DocumentState | null {
    return this.transitionDocumentStatus(documentId, DocumentEvent.APPROVE);
  }

  /**
   * Publish document
   */
  publishDocument(documentId: string): DocumentState | null {
    return this.transitionDocumentStatus(documentId, DocumentEvent.PUBLISH);
  }
}

// Placeholder for MessageBus interface (to be implemented with actual MessageBus)
interface MessageBus {
  publish(message: AgentMessage): Promise<void>;
  subscribe(agent: AgentType, handler: MessageHandler): void;
  unsubscribe(agent: AgentType, handler: MessageHandler): void;
}

// Singleton instance
export const managerAgent = new ManagerAgent();