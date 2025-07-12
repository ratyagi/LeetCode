# Approach: first sort then find first index more than or equal to its value. that is h index
# Time: O(nlogn)
# Space: O(1)

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        sorted_arr = sorted(citations, reverse = True)
        h = 0

        while h < len(sorted_arr) and h < sorted_arr[h]:
            h+=1
        return 

# Test case
print(Solution().hIndex([3, 3, 3]))  # Expected Output: 3
