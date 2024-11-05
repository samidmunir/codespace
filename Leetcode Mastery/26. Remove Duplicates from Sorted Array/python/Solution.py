from typing import List

"""
    Runtime: 0 ms
     - beats 100.00%
    Memory: 17.93 MB
     - beats 50.20%
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = -500
        i = 0
        ptr = 0
        while i < len(nums):
            if nums[i] == last_seen:
                i += 1
            else:
                nums[ptr] = nums[i] 
                last_seen = nums[i]
                ptr += 1
                i += 1
        return ptr
    
    # k = removeDuplicates(self = True, nums = [0, 1, 1, 2, 3, 3, 4])
    k = removeDuplicates(self = True, nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print('\nk:', k)