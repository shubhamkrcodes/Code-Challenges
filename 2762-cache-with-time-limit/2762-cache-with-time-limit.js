var TimeLimitedCache = function() {
    this.store = new Map(); // key -> { value, expiresAt }
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const expiresAt = now + duration;

    let existed = false;
    if (this.store.has(key)) {
        const entry = this.store.get(key);
        if (entry.expiresAt > now) {
            existed = true; // non-expired key exists
        }
    }
    this.store.set(key, { value, expiresAt });
    return existed;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();
    if (this.store.has(key)) {
        const entry = this.store.get(key);
        if (entry.expiresAt > now) {
            return entry.value;
        } else {
            this.store.delete(key); // clean expired
        }
    }
    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;
    for (const [key, entry] of this.store) {
        if (entry.expiresAt > now) {
            count++;
        } else {
            this.store.delete(key); // clean expired
        }
    }
    return count;
};

/**
 * Example usage:
 * const timeLimitedCache = new TimeLimitedCache();
 * console.log(timeLimitedCache.set(1, 42, 1000)); // false
 * console.log(timeLimitedCache.get(1)); // 42
 * console.log(timeLimitedCache.count()); // 1
 */
