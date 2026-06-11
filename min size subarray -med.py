class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total , l=0,0
        res = float("inf")

        for r in range(len(nums)):
            total+= nums[r]
            # if total > = target meaning valid then shift left pointer
            while total >= target:
                res = min(res, (r-l)+1)
                total -= nums[l]
                l+=1
            # if total < target meaning invalid then shift right pointer
        return 0 if res == float("inf") else res

        
