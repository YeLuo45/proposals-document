/**
 * Document State Interface and Status Constants
 */

import { DocumentStatus, DocumentEvent } from './agent';

/**
 * Document State
 */
export interface DocumentState {
  id: string;
  title: string;
  content: string;
  status: DocumentStatus;
  conversationId: string;
  history: HistoryEntry[];
  context: Record<string, any>;
}

export interface HistoryEntry {
  event: DocumentEvent;
  timestamp: number;
  fromStatus: DocumentStatus;
  toStatus: DocumentStatus;
  agent?: string;
  data?: any;
}

/**
 * State transition table
 */
const TRANSITIONS: Record<DocumentStatus, Partial<Record<DocumentEvent, DocumentStatus>>> = {
  [DocumentStatus.DRAFT]: {
    [DocumentEvent.SAVE]: DocumentStatus.DRAFT,
    [DocumentEvent.SUBMIT_FOR_REVIEW]: DocumentStatus.IN_REVIEW
  },
  [DocumentStatus.IN_REVIEW]: {
    [DocumentEvent.REVIEW_PASS]: DocumentStatus.REVISED,
    [DocumentEvent.REVIEW_REJECT]: DocumentStatus.REJECTED
  },
  [DocumentStatus.REVISED]: {
    [DocumentEvent.SAVE]: DocumentStatus.REVISED,
    [DocumentEvent.APPROVE]: DocumentStatus.APPROVED,
    [DocumentEvent.REVISE]: DocumentStatus.DRAFT
  },
  [DocumentStatus.APPROVED]: {
    [DocumentEvent.PUBLISH]: DocumentStatus.PUBLISHED
  },
  [DocumentStatus.PUBLISHED]: {
    [DocumentEvent.SAVE]: DocumentStatus.PUBLISHED
  },
  [DocumentStatus.REJECTED]: {
    [DocumentEvent.REVISE]: DocumentStatus.DRAFT
  }
};

/**
 * Validate and transition document state
 */
export function transition(
  state: DocumentStatus,
  event: DocumentEvent
): DocumentStatus | null {
  const nextStates = TRANSITIONS[state];
  if (!nextStates) {
    return null;
  }
  const nextStatus = nextStates[event];
  return nextStatus || null;
}

/**
 * Check if transition is valid
 */
export function canTransition(state: DocumentStatus, event: DocumentEvent): boolean {
  return transition(state, event) !== null;
}

/**
 * Get available events for a given state
 */
export function getAvailableEvents(state: DocumentStatus): DocumentEvent[] {
  const nextStates = TRANSITIONS[state];
  if (!nextStates) {
    return [];
  }
  return Object.keys(nextStates) as DocumentEvent[];
}