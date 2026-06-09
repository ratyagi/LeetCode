class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # zeroth and last row pattern: (n-1)*2
        # all the rows in the middle will have 2 chars in the zig-zag pattern
        # as we go down (i.e, from row 1 to 2) we need to reduce our jumps by 2. in the 1st row the jums are 4 and then the 2nd row the jumps are 2.  
        # if not last row then the pattern is (n-1)* - 2r. [r = row num]
        if numRows == 1: return s

        res = ""

        for r in range(numRows):
            jump = (numRows -1)*2
            for i in range(r, len(s), jump):
                res += s[i]
                if r>0 and r<numRows-1 and i+jump -2*r < len(s):
                    res+= s[i+jump-2*r]
        
        return res
