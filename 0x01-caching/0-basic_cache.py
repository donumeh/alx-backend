#!/usr/bin/env python3

"""
BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Caching system
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
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
