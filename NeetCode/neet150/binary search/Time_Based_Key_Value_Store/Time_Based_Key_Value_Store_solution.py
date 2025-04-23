from typing import List
import bisect

class TimeMap:

    def __init__(self):
        # Dictionary where each key maps to a list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        # Binary search to find rightmost value less than or equal to timestamp
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return res