# Approach: Greedy + BFS-style Level Traversal
# Time: O(n)
# Space: O(1)
# Thought: Track current range, jump to farthest reachable

class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) -1: 
            farthest = 0
            for i in range (l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res +=1
        return res

# test case
print(Solution().jump([2, 3, 1, 1, 4]))  # Expected output: 2
