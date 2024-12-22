#!/usr/bin/env python3

"""
LFUCache caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache: a caching system that updates the
    least frequently accessed values

    Parent Class:
        BaseCaching: Skeleton for our caching system
    """

    __lfu_metadata = {}

    def __init__(self):
        """
        Initializes the LFU Cache as well as the parent class

        Args:
            self: instance of object

        Return:
            None
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """

        if key is None or item is None:
            return

        metadata = LFUCache.__lfu_metadata

        if key in self.cache_data:
            self.cache_data[key] = item
            metadata[key] = metadata.get(key) + 1
        elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
            self.cache_data[key] = item
            metadata[key] = 0
        else:
            min_lfu = min(v for v in metadata.values())
            for m_key, m_value in metadata.items():
                if m_value == min_lfu:
                    min_lfu_key = m_key
                    break
            print("DISCARD: {}".format(min_lfu_key))
            del self.cache_data[min_lfu_key]
            del metadata[min_lfu_key]
            self.cache_data[key] = item
            metadata[key] = 0

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        metadata = LFUCache.__lfu_metadata
        metadata[key] = metadata[key] + 1
        return self.cache_data.get(key)
