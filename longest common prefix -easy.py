class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #we will first take the first string in the list strs
        #we will start checking if the first letter is present in the rest of the strings. 
        #we will get our results in 2 cases, 
        #(1) the letter we are checking for is out of bounds in the string we are checking for
        #(2) the letter we are checking for does not match in the string we are checking for. 
        # if either case hits. we return the string. 
        res =""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

        
