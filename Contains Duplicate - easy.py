class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # lenght of the array
        n = len(nums)
        # create an empty set
        # Why set()? - they are unique collection of elements. 
        s = set() 
        for i in range(0, n):
            s.add(nums[i])

        return len(s) != len(nums)

        