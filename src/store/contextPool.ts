/**
 * ContextPool - Document context storage with concurrency control
 */

interface ContextData {
  content: any;
  timestamp: number;
  locks: Set<string>;
}

export class ContextPool {
  private storage: Map<string, ContextData> = new Map();
  private useLocalStorage: boolean = false;

  constructor(useLocalStorage: boolean = false) {
    this.useLocalStorage = typeof window !== 'undefined' && useLocalStorage;
  }

  /**
   * Save context for a document
   */
  saveContext(docId: string, context: any): void {
    const data: ContextData = {
      content: context,
      timestamp: Date.now(),
      locks: new Set()
    };

    if (this.useLocalStorage) {
      try {
        localStorage.setItem(`context_${docId}`, JSON.stringify(data));
      } catch (err) {
        console.warn('[ContextPool] localStorage save failed, using memory:', err);
        this.storage.set(docId, data);
      }
    } else {
      this.storage.set(docId, data);
    }
  }

  /**
   * Load context for a document
   */
  loadContext(docId: string): any | null {
    let data: ContextData | undefined;

    if (this.useLocalStorage) {
      try {
        const stored = localStorage.getItem(`context_${docId}`);
        if (stored) {
          data = JSON.parse(stored);
        }
      } catch (err) {
        console.warn('[ContextPool] localStorage load failed:', err);
        data = this.storage.get(docId);
      }
    } else {
      data = this.storage.get(docId);
    }

    return data?.content ?? null;
  }

  /**
   * Clear context for a document
   */
  clearContext(docId: string): void {
    if (this.useLocalStorage) {
      try {
        localStorage.removeItem(`context_${docId}`);
      } catch (err) {
        console.warn('[ContextPool] localStorage clear failed:', err);
      }
    }
    this.storage.delete(docId);
  }

  /**
   * Acquire a lock for a document
   * Returns true if lock acquired, false if already locked
   */
  acquireLock(docId: string, lockId: string = 'default'): boolean {
    let data = this.storage.get(docId);

    if (!data) {
      if (this.useLocalStorage) {
        try {
          const stored = localStorage.getItem(`context_${docId}`);
          if (stored) {
            data = JSON.parse(stored);
          }
        } catch (err) {
          // ignore
        }
      }
    }

    if (!data) {
      // Create new entry if doesn't exist
      data = {
        content: null,
        timestamp: Date.now(),
        locks: new Set()
      };
      this.storage.set(docId, data);
    }

    if (data.locks.has(lockId)) {
      return false; // Already locked by this ID
    }

    // Check if there are any existing locks
    if (data.locks.size > 0) {
      return false; // Document is locked by someone else
    }

    data.locks.add(lockId);
    return true;
  }

  /**
   * Release a lock for a document
   */
  releaseLock(docId: string, lockId: string = 'default'): boolean {
    const data = this.storage.get(docId);
    if (!data) {
      return false;
    }

    if (!data.locks.has(lockId)) {
      return false; // Don't have this lock
    }

    data.locks.delete(lockId);
    return true;
  }

  /**
   * Check if a document is locked
   */
  isLocked(docId: string): boolean {
    const data = this.storage.get(docId);
    if (!data) return false;
    return data.locks.size > 0;
  }

  /**
   * Get all locked document IDs
   */
  getLockedDocuments(): string[] {
    const locked: string[] = [];
    for (const [docId, data] of this.storage.entries()) {
      if (data.locks.size > 0) {
        locked.push(docId);
      }
    }
    return locked;
  }

  /**
   * Update context without affecting locks
   */
  updateContext(docId: string, context: any): void {
    const data = this.storage.get(docId);
    if (data) {
      data.content = context;
      data.timestamp = Date.now();
    }
  }

  /**
   * Get timestamp of last context update
   */
  getLastUpdate(docId: string): number | null {
    const data = this.storage.get(docId);
    return data?.timestamp ?? null;
  }
}

// Singleton instance
export const contextPool = new ContextPool();