#!/usr/bin/env python3
"""4. MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def put(self, key, item):
        """Add an item in the cache"""
        cache = self.cache_data
        if key and item:
            if len(cache) == self.MAX_ITEMS and key not in cache:
                old_key = list(cache.keys())[-1]
                print(f"DISCARD: {old_key}")
                del cache[old_key]
            if key in cache:
                del cache[key]
            cache[key] = item

    def get(self, key):
        """Get an item by key"""
        val = self.cache_data.get(key)
        if val:
            del self.cache_data[key]
            self.cache_data[key] = val
        return val
