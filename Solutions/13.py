def romanToInt(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    n = len(s)
    total = roman[s[n-1]]
    for i in range(n-1):
        if roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total

def main():
    s = "LVIII"
    print(romanToInt(s))

main()