#!/usr/bin/env python3

"""
FIFOCache Module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and is a caching system
    """

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
            first_item = list(self.cache_data.keys())[0]
            del self.cache_data[first_item]
            print(f"DISCARD {first_item}")

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
