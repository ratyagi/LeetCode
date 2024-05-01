# finding the difference in the list. 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            compliment = target - num
            # difference should be in list and its index should not be equal to num's index
            if (compliment in nums and nums.index(compliment) != i):
                    return [i,  nums.index(compliment)]
