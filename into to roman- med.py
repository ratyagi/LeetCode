class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX","V", "IV", "I"]
        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result

# Greedy: largest to smallest, take as many of each symbol as fit.
# Works because subtractive forms (CM, CD, XC, XL, IX, IV) are in the table.
# Time:  O(1) 
# Space: O(1)
