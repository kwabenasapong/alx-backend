#!/usr/bin/env python3

""" 2-lifo_cache.py
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.keys[-1]]
                    print("DISCARD: {}".format(self.keys[-1]))
                    self.keys.pop(-1)
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
