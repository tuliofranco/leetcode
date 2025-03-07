from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_list = []
        for index, value in enumerate(nums):
            if value == val:
                index_list.append(index)
                
        for i in reversed(index_list):
            del nums[i]
        
        return len(nums)