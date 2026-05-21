/**
 * App.tsx - Document Editor with Multi-Agent System Integration
 * 
 * Integrates AgentLoop and ManagerAgent into the Editor UI.
 * Shows current document status and triggers collaborative workflow.
 */

import React, { useState, useEffect, useCallback, useRef } from 'react';
import { v4 as uuidv4 } from 'uuid';
import { AgentLoop, agentLoop } from './agents/agentLoop';
import { messageBus } from './agents/messageBus';
import { managerAgent } from './agents/manager';
import { contextPool } from './store/contextPool';
import { 
  AgentType, 
  MessageType, 
  DocumentStatus, 
  DocumentEvent,
  AgentMessage,
  AgentResult 
} from './types/agent';
import { DocumentState, getAvailableEvents, transition } from './types/document';

// Document status display configuration
const STATUS_CONFIG: Record<DocumentStatus, { label: string; color: string; bgColor: string }> = {
  [DocumentStatus.DRAFT]: { label: 'DRAFT', color: '#6b7280', bgColor: '#f3f4f6' },
  [DocumentStatus.IN_REVIEW]: { label: 'IN REVIEW', color: '#d97706', bgColor: '#fef3c7' },
  [DocumentStatus.REVISED]: { label: 'REVISED', color: '#7c3aed', bgColor: '#ede9fe' },
  [DocumentStatus.APPROVED]: { label: 'APPROVED', color: '#059669', bgColor: '#d1fae5' },
  [DocumentStatus.PUBLISHED]: { label: 'PUBLISHED', color: '#2563eb', bgColor: '#dbeafe' },
  [DocumentStatus.REJECTED]: { label: 'REJECTED', color: '#dc2626', bgColor: '#fee2e2' }
};

// Status flow for visual display
const STATUS_FLOW = [
  DocumentStatus.DRAFT,
  DocumentStatus.IN_REVIEW,
  DocumentStatus.REVISED,
  DocumentStatus.APPROVED,
  DocumentStatus.PUBLISHED
];

interface AppState {
  documentId: string;
  title: string;
  content: string;
  status: DocumentStatus;
  conversationId: string;
  isProcessing: boolean;
  agentMessages: AgentMessage[];
  contextData: any;
}

export default function App() {
  // Document state
  const [state, setState] = useState<AppState>({
    documentId: uuidv4(),
    title: 'Untitled Document',
    content: '',
    status: DocumentStatus.DRAFT,
    conversationId: uuidv4(),
    isProcessing: false,
    agentMessages: [],
    contextData: null
  });

  // Agent loop unsubscribe ref
  const unsubscribeRef = useRef<(() => void) | null>(null);

  // Initialize Agent system on mount
  useEffect(() => {
    console.log('[App] Initializing Agent system...');

    // Subscribe to AgentLoop state changes
    unsubscribeRef.current = agentLoop.subscribe((loopState) => {
      console.log('[App] AgentLoop state changed:', loopState);
      
      setState(prev => ({
        ...prev,
        isProcessing: loopState.isProcessing,
        status: loopState.currentStatus
      }));
    });

    // Start ManagerAgent
    managerAgent.listen();

    // Create document in AgentLoop
    agentLoop.createDocument(
      state.documentId,
      state.title,
      state.conversationId
    );

    // Subscribe to messages
    messageBus.subscribe(AgentType.MANAGER, handleManagerMessage);

    console.log('[App] Agent system initialized');

    // Cleanup on unmount
    return () => {
      if (unsubscribeRef.current) {
        unsubscribeRef.current();
      }
      managerAgent.stop();
      messageBus.unsubscribe(AgentType.MANAGER, handleManagerMessage);
      console.log('[App] Agent system cleaned up');
    };
  }, []);

  // Handle messages from ManagerAgent
  const handleManagerMessage = useCallback(async (message: AgentMessage) => {
    console.log('[App] Manager message received:', message.type);

    setState(prev => ({
      ...prev,
      agentMessages: [...prev.agentMessages, message]
    }));

    // Process based on message type
    switch (message.type) {
      case MessageType.REVIEW_REQUEST:
        console.log('[App] Review requested for document');
        break;
      case MessageType.APPROVAL_REQUEST:
        console.log('[App] Approval requested');
        break;
      case MessageType.ERROR:
        console.error('[App] Error from agent:', message.payload);
        break;
    }
  }, []);

  // Handle content change
  const handleContentChange = useCallback((newContent: string) => {
    setState(prev => ({ ...prev, content: newContent }));
    
    // Update in AgentLoop
    agentLoop.updateContent(state.documentId, newContent);
    
    // Save to context pool
    contextPool.saveContext(state.documentId, {
      content: newContent,
      timestamp: Date.now()
    });
  }, [state.documentId]);

  // Handle title change
  const handleTitleChange = useCallback((newTitle: string) => {
    setState(prev => ({ ...prev, title: newTitle }));
  }, []);

  // Submit document for review - triggers Manager.submitDocument()
  const handleSubmitForReview = useCallback(() => {
    console.log('[App] Submitting document for review...');
    setState(prev => ({ ...prev, isProcessing: true }));

    // Use AgentLoop to transition status
    const newStatus = transition(state.status, DocumentEvent.SUBMIT_FOR_REVIEW);
    if (newStatus) {
      agentLoop.setDocumentStatus(state.documentId, newStatus);
      
      // Publish message to MessageBus
      messageBus.publish({
        id: uuidv4(),
        sender: AgentType.EDITOR,
        receiver: AgentType.MANAGER,
        type: MessageType.SUBMIT_FOR_REVIEW,
        payload: {
          documentId: state.documentId,
          title: state.title,
          content: state.content,
          conversationId: state.conversationId
        },
        timestamp: Date.now(),
        requiresApproval: false
      });

      setState(prev => ({ 
        ...prev, 
        status: newStatus,
        isProcessing: false 
      }));

      // Dispatch to appropriate agents
      managerAgent.dispatch({
        id: state.documentId,
        title: state.title,
        content: state.content,
        status: newStatus,
        conversationId: state.conversationId,
        history: [],
        context: {}
      });
    }
  }, [state]);

  // Save document
  const handleSave = useCallback(() => {
    console.log('[App] Saving document...');
    
    contextPool.saveContext(state.documentId, {
      document: {
        id: state.documentId,
        title: state.title,
        content: state.content,
        status: state.status
      },
      timestamp: Date.now()
    });

    setState(prev => ({
      ...prev,
      contextData: contextPool.loadContext(state.documentId)
    }));
  }, [state]);

  // Approve document (for testing workflow)
  const handleApprove = useCallback(() => {
    const newStatus = transition(state.status, DocumentEvent.APPROVE);
    if (newStatus) {
      agentLoop.setDocumentStatus(state.documentId, newStatus);
      setState(prev => ({ ...prev, status: newStatus }));
    }
  }, [state]);

  // Publish document (for testing workflow)
  const handlePublish = useCallback(() => {
    const newStatus = transition(state.status, DocumentEvent.PUBLISH);
    if (newStatus) {
      agentLoop.setDocumentStatus(state.documentId, newStatus);
      setState(prev => ({ ...prev, status: newStatus }));
    }
  }, [state]);

  // Get available actions based on current status
  const availableEvents = getAvailableEvents(state.status);
  const statusConfig = STATUS_CONFIG[state.status];

  return (
    <div style={{ 
      minHeight: '100vh', 
      backgroundColor: '#f9fafb',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      {/* Header */}
      <header style={{
        backgroundColor: 'white',
        borderBottom: '1px solid #e5e7eb',
        padding: '16px 24px'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
          <h1 style={{ fontSize: '24px', fontWeight: 600, margin: 0 }}>
            Document Editor V2
          </h1>
          <p style={{ color: '#6b7280', margin: '4px 0 0' }}>
            Multi-Agent Collaborative System
          </p>
        </div>
      </header>

      {/* Status Bar */}
      <div style={{
        backgroundColor: 'white',
        borderBottom: '1px solid #e5e7eb',
        padding: '12px 24px'
      }}>
        <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', alignItems: 'center', gap: '24px' }}>
          {/* Status Display */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '14px', color: '#6b7280' }}>Status:</span>
            <span style={{
              padding: '4px 12px',
              borderRadius: '16px',
              fontSize: '12px',
              fontWeight: 600,
              backgroundColor: statusConfig.bgColor,
              color: statusConfig.color
            }}>
              {statusConfig.label}
            </span>
            {state.isProcessing && (
              <span style={{
                width: '16px',
                height: '16px',
                border: '2px solid #3b82f6',
                borderTopColor: 'transparent',
                borderRadius: '50%',
                animation: 'spin 1s linear infinite'
              }} />
            )}
          </div>

          {/* Status Flow */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', flex: 1 }}>
            {STATUS_FLOW.map((status, index) => {
              const config = STATUS_CONFIG[status];
              const isActive = state.status === status;
              const isPast = STATUS_FLOW.indexOf(state.status) > index;
              
              return (
                <React.Fragment key={status}>
                  {index > 0 && (
                    <div style={{
                      width: '24px',
                      height: '2px',
                      backgroundColor: isPast ? '#10b981' : '#d1d5db'
                    }} />
                  )}
                  <span style={{
                    padding: '2px 8px',
                    borderRadius: '4px',
                    fontSize: '11px',
                    fontWeight: isActive ? 600 : 400,
                    backgroundColor: isActive ? config.bgColor : (isPast ? '#d1fae5' : '#f3f4f6'),
                    color: isActive ? config.color : (isPast ? '#059669' : '#9ca3af')
                  }}>
                    {config.label}
                  </span>
                </React.Fragment>
              );
            })}
          </div>

          {/* Document ID */}
          <span style={{ fontSize: '12px', color: '#9ca3af' }}>
            ID: {state.documentId.slice(0, 8)}...
          </span>
        </div>
      </div>

      {/* Main Content */}
      <main style={{ maxWidth: '1200px', margin: '0 auto', padding: '24px' }}>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 320px', gap: '24px' }}>
          {/* Editor Panel */}
          <div style={{
            backgroundColor: 'white',
            borderRadius: '8px',
            boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
            overflow: 'hidden'
          }}>
            {/* Title Input */}
            <div style={{ padding: '16px', borderBottom: '1px solid #e5e7eb' }}>
              <input
                type="text"
                value={state.title}
                onChange={(e) => handleTitleChange(e.target.value)}
                placeholder="Document Title"
                style={{
                  width: '100%',
                  fontSize: '20px',
                  fontWeight: 600,
                  border: 'none',
                  outline: 'none',
                  backgroundColor: 'transparent'
                }}
              />
            </div>

            {/* Content Editor */}
            <div style={{ padding: '16px', minHeight: '400px' }}>
              <textarea
                value={state.content}
                onChange={(e) => handleContentChange(e.target.value)}
                placeholder="Start writing your document..."
                style={{
                  width: '100%',
                  minHeight: '380px',
                  border: 'none',
                  outline: 'none',
                  resize: 'vertical',
                  fontSize: '14px',
                  lineHeight: '1.6',
                  fontFamily: 'inherit'
                }}
              />
            </div>

            {/* Editor Actions */}
            <div style={{
              padding: '12px 16px',
              borderTop: '1px solid #e5e7eb',
              display: 'flex',
              gap: '8px'
            }}>
              <button
                onClick={handleSave}
                disabled={state.isProcessing}
                style={{
                  padding: '8px 16px',
                  borderRadius: '6px',
                  border: '1px solid #d1d5db',
                  backgroundColor: 'white',
                  fontSize: '14px',
                  cursor: state.isProcessing ? 'not-allowed' : 'pointer',
                  opacity: state.isProcessing ? 0.6 : 1
                }}
              >
                Save
              </button>
              
              {availableEvents.includes(DocumentEvent.SUBMIT_FOR_REVIEW) && (
                <button
                  onClick={handleSubmitForReview}
                  disabled={state.isProcessing}
                  style={{
                    padding: '8px 16px',
                    borderRadius: '6px',
                    border: 'none',
                    backgroundColor: '#2563eb',
                    color: 'white',
                    fontSize: '14px',
                    cursor: state.isProcessing ? 'not-allowed' : 'pointer',
                    opacity: state.isProcessing ? 0.6 : 1
                  }}
                >
                  Submit for Review
                </button>
              )}

              {availableEvents.includes(DocumentEvent.APPROVE) && (
                <button
                  onClick={handleApprove}
                  style={{
                    padding: '8px 16px',
                    borderRadius: '6px',
                    border: 'none',
                    backgroundColor: '#059669',
                    color: 'white',
                    fontSize: '14px',
                    cursor: 'pointer'
                  }}
                >
                  Approve
                </button>
              )}

              {availableEvents.includes(DocumentEvent.PUBLISH) && (
                <button
                  onClick={handlePublish}
                  style={{
                    padding: '8px 16px',
                    borderRadius: '6px',
                    border: 'none',
                    backgroundColor: '#7c3aed',
                    color: 'white',
                    fontSize: '14px',
                    cursor: 'pointer'
                  }}
                >
                  Publish
                </button>
              )}
            </div>
          </div>

          {/* Sidebar */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {/* Agent Status */}
            <div style={{
              backgroundColor: 'white',
              borderRadius: '8px',
              boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
              padding: '16px'
            }}>
              <h3 style={{ fontSize: '14px', fontWeight: 600, margin: '0 0 12px' }}>
                Active Agents
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {Object.values(AgentType).map(agentType => (
                  <div key={agentType} style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '8px'
                  }}>
                    <span style={{
                      width: '8px',
                      height: '8px',
                      borderRadius: '50%',
                      backgroundColor: agentType === AgentType.MANAGER ? '#10b981' : '#6b7280'
                    }} />
                    <span style={{ fontSize: '13px', textTransform: 'capitalize' }}>
                      {agentType}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Message Log */}
            <div style={{
              backgroundColor: 'white',
              borderRadius: '8px',
              boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
              padding: '16px',
              flex: 1,
              maxHeight: '300px',
              overflow: 'auto'
            }}>
              <h3 style={{ fontSize: '14px', fontWeight: 600, margin: '0 0 12px' }}>
                Agent Messages ({state.agentMessages.length})
              </h3>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                {state.agentMessages.slice(-10).map((msg, index) => (
                  <div key={index} style={{
                    padding: '8px',
                    backgroundColor: '#f9fafb',
                    borderRadius: '4px',
                    fontSize: '12px'
                  }}>
                    <span style={{ fontWeight: 600 }}>{msg.type}</span>
                    <span style={{ color: '#6b7280', marginLeft: '8px' }}>
                      from {msg.sender}
                    </span>
                  </div>
                ))}
                {state.agentMessages.length === 0 && (
                  <span style={{ fontSize: '12px', color: '#9ca3af' }}>
                    No messages yet
                  </span>
                )}
              </div>
            </div>

            {/* Context Data */}
            {state.contextData && (
              <div style={{
                backgroundColor: 'white',
                borderRadius: '8px',
                boxShadow: '0 1px 3px rgba(0,0,0,0.1)',
                padding: '16px'
              }}>
                <h3 style={{ fontSize: '14px', fontWeight: 600, margin: '0 0 8px' }}>
                  Context Pool
                </h3>
                <pre style={{
                  fontSize: '11px',
                  backgroundColor: '#f3f4f6',
                  padding: '8px',
                  borderRadius: '4px',
                  overflow: 'auto'
                }}>
                  {JSON.stringify(state.contextData, null, 2)}
                </pre>
              </div>
            )}
          </div>
        </div>
      </main>

      {/* CSS Animation */}
      <style>{`
        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}