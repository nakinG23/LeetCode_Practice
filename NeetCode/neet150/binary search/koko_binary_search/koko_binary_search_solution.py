from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        
        sorted_piles = sorted(piles)
        left, right = 1, sorted_piles[-1]
        print(left,right)
        opt_k = sorted_piles[-1]

        while left<=right:
            mid = (left+right)//2
            hours = 0
            for pile in sorted_piles:
                hours += math.ceil(pile/mid)
            print(mid, hours)
            if hours <= h:
                opt_k = min(opt_k, mid)
                right = mid-1
            else:
                left = mid+1
        return opt_k

"""
koko can eat at most k number of bananas in an hour, if any left, itll take it one more hour to eat them
now, optimal k should be the min value that allows this to happen
within h hours
macx would be the max of piles value, then it will eat in len(piles) time
do binary search and see how long does mid//2 take to eat
"""