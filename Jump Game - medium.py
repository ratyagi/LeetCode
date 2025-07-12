#Greedy approach
# time: O(n)
# space: O(1)
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        Goalpost = len (nums) -1

        for i in range(len(nums)-1, -1, -1):
            if i+ nums[i] >= Goalpost:
                Goalpost = i

        return True if Goalpost == 0 else False

# Test case
print(Solution().canJump([2, 3, 1, 1, 4]))  # Output: True





'''
DP top down approach with memo
#Time: O(n^2)
#Space: O(n)
class Solution: 
    def canJump(self, nums: list[int]) -> bool:
        n= len(nums)
        memo = {n - 1: True}  # Only the last index is reachable from itself
        def can_reach(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):  # Try all jumps
                if i + jump < n and can_reach(i + jump):  # Check if any jump leads to success
                    memo[i] = True
                    return True

            memo[i] = False
            return False
        return can_reach(0)
-------------------------------------------------
CALL FLOW for top-down DP approach with memo
call: can_reach(0)
  nums[0] = 3 → jumps: 1, 2, 3
  try jump=1 → call: can_reach(1)
    nums[1] = 2 → jumps: 1, 2
    try jump=1 → call: can_reach(2)
      nums[2] = 1 → jumps: 1
      try jump=1 → call: can_reach(3)
        nums[3] = 0 → jumps: 0
        no jumps possible
      → can_reach(3) returns False, memo[3] = False
    → can_reach(2) returns False, memo[2] = False
    try jump=2 → call: can_reach(3)
      found in memo: False
    → can_reach(1) returns False, memo[1] = False
  try jump=2 → call: can_reach(2)
    found in memo: False
  try jump=3 → call: can_reach(3)
    found in memo: False
→ can_reach(0) returns False, memo[0] = False
'''
