// Agent Type Definitions for doc-editor V2 Multi-Agent System

export enum AgentType {
  EDITOR = 'editor',
  REVIEWER = 'reviewer',
  RESEARCHER = 'researcher',
  MANAGER = 'manager'
}

export enum MessageType {
  EDIT_REQUEST = 'EDIT_REQUEST',
  REVIEW_REQUEST = 'REVIEW_REQUEST',
  RESEARCH_REQUEST = 'RESEARCH_REQUEST',
  ORCHESTRATE = 'ORCHESTRATE',
  APPROVAL_REQUEST = 'APPROVAL_REQUEST',
  APPROVAL_RESPONSE = 'APPROVAL_RESPONSE',
  ERROR = 'ERROR'
}

export enum DocumentStatus {
  DRAFT = 'DRAFT',
  IN_REVIEW = 'IN_REVIEW',
  REVISED = 'REVISED',
  APPROVED = 'APPROVED',
  PUBLISHED = 'PUBLISHED',
  REJECTED = 'REJECTED'
}

export interface AgentMessage {
  id: string;
  sender: AgentType;
  receiver: AgentType | 'broadcast';
  type: MessageType;
  payload: any;
  timestamp: number;
  requiresApproval?: boolean;
  conversationId?: string;
  parentId?: string;
}

export interface Document {
  id: string;
  title: string;
  content: string;
  status: DocumentStatus;
  createdAt: number;
  updatedAt: number;
  authorId?: string;
}

export interface AgentState {
  agentId: string;
  agentType: AgentType;
  status: 'idle' | 'working' | 'blocked' | 'offline';
  currentTask?: string;
  lastUpdate: number;
}

// Tool definition for Agent execution
export interface ToolDefinition {
  name: string;
  description: string;
  parameters: Record<string, any>;
  execute: (args: any) => Promise<string>;
}

// State transition for document workflow
export interface StateTransition {
  from: DocumentStatus;
  to: DocumentStatus;
  trigger: AgentType;
  action?: string;
}

export const DOCUMENT_STATE_MACHINE: Record<DocumentStatus, DocumentStatus[]> = {
  [DocumentStatus.DRAFT]: [DocumentStatus.IN_REVIEW],
  [DocumentStatus.IN_REVIEW]: [DocumentStatus.REVISED, DocumentStatus.REJECTED],
  [DocumentStatus.REVISED]: [DocumentStatus.APPROVED, DocumentStatus.DRAFT],
  [DocumentStatus.APPROVED]: [DocumentStatus.PUBLISHED],
  [DocumentStatus.PUBLISHED]: [],
  [DocumentStatus.REJECTED]: [DocumentStatus.DRAFT]
};