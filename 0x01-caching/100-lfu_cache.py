#!/usr/bin/env python3

""" 100-lfu_cache.py
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.keys = []
        self.occurrences = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.occurrences[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_occurrence = min(self.occurrences.values())
                    for key in self.occurrences:
                        if self.occurrences[key] == min_occurrence:
                            del self.cache_data[key]
                            del self.occurrences[key]
                            print("DISCARD: {}".format(key))
                            break
                self.cache_data[key] = item
                self.occurrences[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.occurrences[key] += 1
            return self.cache_data[key]
        return None
