// AgentLoop - Core session management and context building

import { v4 as uuidv4 } from 'uuid';
import { AgentMessage, AgentType, DocumentStatus } from '../types/agent';
import { DocumentState } from '../types/document';
import { DOCUMENT_STATE_MACHINE } from '../types/agent';

export interface AgentLoopState {
  sessionId: string;
  documentId: string | null;
  currentStatus: DocumentStatus;
  isProcessing: boolean;
  messages: AgentMessage[];
  lastUpdate: number;
}

type StateChangeHandler = (state: AgentLoopState) => void;

export class AgentLoop {
  private state: AgentLoopState;
  private listeners: Set<StateChangeHandler> = new Set();
  private documents: Map<string, DocumentState> = new Map();

  constructor() {
    this.state = {
      sessionId: uuidv4(),
      documentId: null,
      currentStatus: DocumentStatus.DRAFT,
      isProcessing: false,
      messages: [],
      lastUpdate: Date.now()
    };
  }

  getState(): AgentLoopState {
    return { ...this.state };
  }

  getState(docId: string): DocumentState | undefined {
    return this.documents.get(docId);
  }

  subscribe(handler: StateChangeHandler): () => void {
    this.listeners.add(handler);
    return () => this.listeners.delete(handler);
  }

  private notify(): void {
    this.state.lastUpdate = Date.now();
    for (const handler of this.listeners) {
      handler(this.getState());
    }
  }

  createDocument(docId: string, title: string, conversationId: string): DocumentState {
    const docState: DocumentState = {
      id: docId,
      title,
      content: '',
      status: DocumentStatus.DRAFT,
      conversationId,
      history: [],
      context: {}
    };
    this.documents.set(docId, docState);
    this.state.documentId = docId;
    this.state.currentStatus = DocumentStatus.DRAFT;
    this.notify();
    return docState;
  }

  updateContent(docId: string, content: string): void {
    const doc = this.documents.get(docId);
    if (doc) {
      doc.content = content;
      this.notify();
    }
  }

  setDocumentStatus(docId: string, status: DocumentStatus): boolean {
    const doc = this.documents.get(docId);
    if (!doc) return false;

    const allowedTransitions = DOCUMENT_STATE_MACHINE[doc.status] || [];
    if (allowedTransitions.includes(status)) {
      doc.status = status;
      this.state.currentStatus = status;
      this.notify();
      return true;
    }
    return false;
  }

  setDocument(doc: { id: string; title: string; content?: string; status: DocumentStatus; conversationId: string }): void {
    const docState: DocumentState = {
      id: doc.id,
      title: doc.title,
      content: doc.content || '',
      status: doc.status,
      conversationId: doc.conversationId,
      history: [],
      context: {}
    };
    this.documents.set(doc.id, docState);
    this.state.documentId = doc.id;
    this.state.currentStatus = doc.status;
    this.notify();
  }

  updateStatus(status: DocumentStatus): boolean {
    const allowedTransitions = DOCUMENT_STATE_MACHINE[this.state.currentStatus] || [];
    if (allowedTransitions.includes(status)) {
      this.state.currentStatus = status;
      if (this.state.documentId) {
        const doc = this.documents.get(this.state.documentId);
        if (doc) {
          doc.status = status;
        }
      }
      this.notify();
      return true;
    }
    return false;
  }

  setProcessing(processing: boolean): void {
    this.state.isProcessing = processing;
    this.notify();
  }

  addMessage(message: AgentMessage): void {
    this.state.messages.push(message);
    this.notify();
  }

  reset(): void {
    this.state = {
      sessionId: uuidv4(),
      documentId: null,
      currentStatus: DocumentStatus.DRAFT,
      isProcessing: false,
      messages: [],
      lastUpdate: Date.now()
    };
    this.documents.clear();
    this.notify();
  }
}

// Singleton instance
export const agentLoop = new AgentLoop();