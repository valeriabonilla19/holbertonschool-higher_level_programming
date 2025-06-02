#!/usr/bin/env python3
"""A CountedIterator that counts how many items have been iterated over."""

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # May raise StopIteration, which is correct
        self.count += 1
        return item

    def get_count(self):
        return self.count
