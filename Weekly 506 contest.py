# Q1, Q2, Q3 Accepted. Q4 exceeded time limit
# Language used: Python3/ python

# QUESTION 1

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0
        while n >0:
            d= n% 10
            digit_sum+=d
            square_sum+=d*d
            n//=10
        return square_sum-digit_sum>=50
        

# QUESTION 2

from typing import List
class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        for i in range(n):
            cnt = {}
            fof = {}
            maxf =0
            distinct = 0
            for j in range (i, n):
                v = nums[j]
                f = cnt.get(v,0)
                if f>0:
                    fof[f] -=1
                    if fof[f]==0:
                        del fof[f]
                else: 
                    distinct +=1
                f+=1
                cnt[v] =f
                fof[f] = fof.get(f,0)+1
                if f>maxf:
                    maxf = f
                if distinct == 1:
                    ok = True
                else:
                    half = maxf//2
                    ok = (maxf % 2 == 0 and fof.get(half, 0) > 0 and fof.get(maxf, 0) +fof.get(half, 0) == distinct)
                
                if ok:
                    best = max(best, j - i + 1)
        return best
        


# QUESTION 3


class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        total_best =0
        global_min = float('inf')
        min_best = float('inf')

        for row in units:
            m1 = m2 = float('inf')
            for v in row:
                if v<m1:
                    m2, m1 = m1, v
                elif v< m2:
                    m2 = v
            if len(row) ==1:
                m2=0

            best = max(m1, m2)
            total_best += best
            global_min = min (global_min, m1)
            min_best = min (min_best, best)
        return global_min + total_best - min_best

# QUESTION 4


from sortedcontainers import SortedList
class Solution(object):
    def maxSum(self, nums, k):
        n = len(nums)
        ans =float('-inf')
        for l in range(n):
            inside = SortedList()
            outside = SortedList(nums)
            isum = 0
            for r in range(l, n):
                v = nums[r]
                outside.remove(v)
                inside.add(v)
                isum += v
                gain = 0 
                L = len(inside)
                out_len = len(outside)
                s = 0
                while s<k and s <L and s< out_len:
                    out_val = outside[out_len -1 -s]
                    in_val = inside[s]
                    if out_val > in_val:
                        gain+= out_val - in_val
                        s+=1
                    else:
                        break
                ans = max(ans, isum +gain)
        return ans
