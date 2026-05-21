// MessageBus - Async message routing system (nanobot-style)

import { AgentMessage, AgentType } from '../types/agent';

type MessageHandler = (message: AgentMessage) => Promise<void>;

export class MessageBus {
  private queue: AgentMessage[] = [];
  private subscribers: Map<AgentType, MessageHandler[]> = new Map();
  private processing: boolean = false;

  constructor() {
    this.subscribers.set(AgentType.MANAGER, []);
    this.subscribers.set(AgentType.EDITOR, []);
    this.subscribers.set(AgentType.REVIEWER, []);
    this.subscribers.set(AgentType.RESEARCHER, []);
  }

  async publish(message: AgentMessage): Promise<void> {
    this.queue.push(message);
    if (!this.processing) {
      this.processQueue();
    }
  }

  subscribe(agent: AgentType, handler: MessageHandler): void {
    const handlers = this.subscribers.get(agent) || [];
    handlers.push(handler);
    this.subscribers.set(agent, handlers);
  }

  unsubscribe(agent: AgentType, handler: MessageHandler): void {
    const handlers = this.subscribers.get(agent) || [];
    const index = handlers.indexOf(handler);
    if (index > -1) {
      handlers.splice(index, 1);
    }
  }

  private async processQueue(): Promise<void> {
    this.processing = true;
    while (this.queue.length > 0) {
      const message = this.queue.shift();
      if (!message) continue;

      const handlers = this.subscribers.get(message.receiver as AgentType) || [];
      if (message.receiver === 'broadcast') {
        for (const [agent, agentHandlers] of this.subscribers.entries()) {
          for (const handler of agentHandlers) {
            try {
              await handler(message);
            } catch (error) {
              console.error(`Handler error for ${agent}:`, error);
            }
          }
        }
      } else {
        for (const handler of handlers) {
          try {
            await handler(message);
          } catch (error) {
            console.error(`Handler error:`, error);
          }
        }
      }
    }
    this.processing = false;
  }

  getQueueLength(): number {
    return this.queue.length;
  }

  clear(): void {
    this.queue = [];
  }
}

// Singleton instance
export const messageBus = new MessageBus();