class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #edge: if we have an empty string as needle then we return 0
        # whenever we have to check some consecutive chars in a string we do arr[i:i+ len(string of chars we wanna check)] == strings of char we wanna check
        if needle == "": return 0
        for i in range (len(haystack)-len(needle)+1):
            if haystack[i:i+ len(needle)] == needle:
                return i
        return -1

#Time: O(n*m)
#space: O(1)
# better solution through KMP, but i am not implementing it. 
