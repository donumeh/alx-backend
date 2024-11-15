#!/usr/bin/env python3

"""
LRUCache Module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache: a caching system
    """

    __counter = 0
    __access_counter = {}

    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            return

        a_key = None
        if (
            len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            least_used = min(list(LRUCache.__access_counter.values()))
            for k, v in LRUCache.__access_counter.items():
                if least_used == v:
                    a_key = k
                    del self.cache_data[k]
                    break
            print(f"DISCARD: {a_key}")

        if a_key:
            del LRUCache.__access_counter[a_key]
        self.cache_data[key] = item
        LRUCache.__access_counter[key] = LRUCache.__counter
        LRUCache.__counter += 1

    def get(self, key):
        """
        Get an item by key
        """

        value = self.cache_data.get(key, None)
        if value:
            LRUCache.__access_counter[key] = LRUCache.__counter
            LRUCache.__counter += 1
        return value
