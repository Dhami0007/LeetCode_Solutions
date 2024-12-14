def plusOne(digits):
    carry = 1
    n = len(digits)
    i = 0 
    condition = False
    while i < n and condition == False:
        ans = digits[n-1-i] + carry
        print(ans)
        if ans > 9:
            carry = 1
            digits[n-1-i] = 0
        else:
            carry = 0
            digits[n-1-i] = ans
            condition = True
        i += 1
    
    if carry == 1:
        return [1] + digits
    return digits

def main():
    digits = [8,9,9,9]
    print(plusOne(digits))

main()