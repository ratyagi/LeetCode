class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers: if sum is greater then target then shift left and f it is small then shift right. 

        l, r = 0, len(numbers)-1
        while l<r:
            curSum = numbers[l] + numbers[r]

            if curSum < target:
                l+=1
            elif curSum > target:
                r-=1
            else: return [l+1, r+1]

# time: O(n)
# space: O(1)
        
