# initially I compared i and i+1. if similar then pop i+1 - NOT optimum!
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i < len(nums):
            if i== len(nums)-1:
                break
            else:
                if nums[i] == nums[i+1]:
                    nums.pop(i+1)
                else: 
                    i+=1
        return (len(nums))
        
# Optimum sol -> overwrite unique elem
# i=0 and j(1, len(nums)). if not equal, i++ and transfer j's val into i
# if equal, i stays where it is and j++(next iteration)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j] 
        return i + 1 


# Test the function
solution = Solution()
print(solution.removeDuplicates(nums= [0,0,1,1,1,2,2,3,3,4]))