
def romanToInt(s: str) -> int:
    romanSymbol = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    for cur in range(len(s)-1):
        if romanSymbol[s[cur]] < romanSymbol[s[cur+1]]:
            total -= romanSymbol[s[cur]]
        else:
            total += romanSymbol[s[cur]]
    
    total += romanSymbol[s[-1]]
    return total   

print(romanToInt("XIV"))      # Expected output: 14
print(romanToInt("XIX"))      # Expected output: 19
print(romanToInt("XLII"))     # Expected output: 42
print(romanToInt("LVIII"))    # Expected output: 58
print(romanToInt("MCMXCIV"))  # Expected output: 1994
print(romanToInt("MMXXIV"))   # Expected output: 2024