#!/usr/bin/env python3
"""5. LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""
    freq = {}

    def put(self, key, item):
        """Add an item in the cache"""
        cache = self.cache_data
        if key and item:
            if len(cache) == self.MAX_ITEMS and key not in cache:
                sort = dict(sorted(self.freq.items(), key=lambda i: i[1]))
                keys = [i for i in sort if sort[i] == sort[next(iter(sort))]]
                if len(keys) == 1:
                    old_key = keys[0]
                else:
                    for k in list(cache.keys()):
                        if k in keys:
                            old_key = k
                            break
                print(f"DISCARD: {old_key}")
                del cache[old_key]
                del self.freq[old_key]
            if key in cache:
                del cache[key]
                self.freq[key] += 1
            else:
                self.freq[key] = 0
            cache[key] = item

    def get(self, key):
        """Get an item by key"""
        val = self.cache_data.get(key)
        if val:
            del self.cache_data[key]
            self.cache_data[key] = val
            self.freq[key] += 1
        return val
