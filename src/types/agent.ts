/**
 * Agent 类型定义
 */

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
  ERROR = 'ERROR',
  RESPONSE = 'RESPONSE',
  SAVE = 'SAVE',
  SUBMIT_FOR_REVIEW = 'SUBMIT_FOR_REVIEW'
}

export enum DocumentStatus {
  DRAFT = 'DRAFT',
  IN_REVIEW = 'IN_REVIEW',
  REVISED = 'REVISED',
  APPROVED = 'APPROVED',
  PUBLISHED = 'PUBLISHED',
  REJECTED = 'REJECTED'
}

export enum DocumentEvent {
  SAVE = 'SAVE',
  SUBMIT_FOR_REVIEW = 'SUBMIT_FOR_REVIEW',
  REVIEW_PASS = 'REVIEW_PASS',
  REVIEW_REJECT = 'REVIEW_REJECT',
  REVISE = 'REVISE',
  APPROVE = 'APPROVE',
  PUBLISH = 'PUBLISH'
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

export interface MessageHandler {
  (message: AgentMessage): Promise<void>;
}

export interface AgentResult {
  success: boolean;
  data?: any;
  error?: string;
  score?: number;
}

/**
 * Document state machine - defines allowed transitions
 */
export const DOCUMENT_STATE_MACHINE: Record<DocumentStatus, DocumentStatus[]> = {
  [DocumentStatus.DRAFT]: [DocumentStatus.IN_REVIEW],
  [DocumentStatus.IN_REVIEW]: [DocumentStatus.REVISED, DocumentStatus.REJECTED],
  [DocumentStatus.REVISED]: [DocumentStatus.APPROVED, DocumentStatus.DRAFT],
  [DocumentStatus.APPROVED]: [DocumentStatus.PUBLISHED],
  [DocumentStatus.PUBLISHED]: [],
  [DocumentStatus.REJECTED]: [DocumentStatus.DRAFT]
};