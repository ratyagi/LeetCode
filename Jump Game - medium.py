class Solution:
    def canJump(self, nums: list[int]) -> bool:
        Goalpost = len (nums) -1

        for i in range(len(nums)-1, -1, -1):
            if i+ nums[i] >= Goalpost:
                Goalpost = i

        return True if Goalpost == 0 else False

# Test case
print(Solution().canJump([2, 3, 1, 1, 4]))  # Output: True
