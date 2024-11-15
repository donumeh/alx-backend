#!/usr/bin/env python3

"""
LIFOCache Module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache is a simple caching system
    """

    __pointer = BaseCaching.MAX_ITEMS - 1

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

        if (
            len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS
            and key not in self.cache_data
        ):
            last_item_added = list(self.cache_data.keys())[LIFOCache.__pointer]
            del self.cache_data[last_item_added]
            print(f"DISCARD: {last_item_added}")

        self.cache_data[key] = item
        LIFOCache.__pointer = list(self.cache_data.keys()).index(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
