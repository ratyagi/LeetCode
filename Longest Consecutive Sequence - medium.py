class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in numSet: # outter loop O(n)
            if (i-1) not in numSet: # O(1)
                seq = 0
                while (i+ seq) in numSet: #O(1)
                    seq+=1
                longest = max (seq, longest)
        return longest
'''
We need: 
    1. Set-> unordered, unique. set is a hash table. so (x in numSet) becomes hash(x) which is O(1).
    2. while (i+1) is incorrect cuz that becomes an infinite loop. it keeps on checking one condition on repeat. 
'''
