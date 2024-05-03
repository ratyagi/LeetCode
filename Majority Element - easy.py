class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
        return nums[n//2]
    
# Test the function
solution = Solution()
print(solution.majorityElement(nums = [8, 6, 8, 10, 8, 20, 10, 8, 8]))
