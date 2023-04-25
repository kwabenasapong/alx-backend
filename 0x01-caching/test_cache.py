#!/usr/bin/env python3

'''test task 3 to 100'''

# import base_caching
BaseCaching = __import__('base_caching').BaseCaching


'''
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least recently used item (LRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''

class LRUCache(BaseCaching):
    '''LRUCache class'''
    def __init__(self):
        '''init method'''
        super().__init__()
        self.keys = []
    
    def put(self, key, item):
        '''put method'''
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.keys[0]]
                    print("DISCARD: {}".format(self.keys[0]))
                    self.keys.pop(0)
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        '''get method'''
        if key in self.cache_data:
            return self.cache_data[key]
        return None
