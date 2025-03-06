from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in nums_dict:
                return [nums_dict[complement], index]
            nums_dict[value] = index