#!/usr/bin/env python3

"""
MRUCache Module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache: a caching system
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
            len(list(self.cache_data.keys())) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            r_used = max(list(MRUCache.__access_counter.values()))

            for k, v in MRUCache.__access_counter.items():
                if v == r_used:
                    del self.cache_data[k]
                    a_key = k
                    break
            print(f"DISCARD: {a_key}")

        if a_key:
            del MRUCache.__access_counter[a_key]

        self.cache_data[key] = item
        # MRUCache.__access_counter[key] = MRUCache.__counter
        # MRUCache.__counter += 1
        MRUCache.increment_counter(key)

    def get(self, key):
        """
        Get an item by key
        """
        value = self.cache_data.get(key, None)

        if value:
            # MRUCache.__access_counter[key] = MRUCache.__counter
            # MRUCache.__counter += 1
            MRUCache.increment_counter(key)

        return value

    @classmethod
    def increment_counter(cls, key):
        MRUCache.__access_counter[key] = MRUCache.__counter
        MRUCache.__counter += 1
