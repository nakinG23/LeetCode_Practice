from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = nums[0]
        
        while left <= right:    
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid - 1
            print (nums[left:right+1])
        return res


"""
number of rotations send n number of elements to the beginnning
123456, rotated 4 times becomes 345612
first we need to figure out the number of rotations
then try and find the min element
123456
234561
345612
456123
561234
612345
"""