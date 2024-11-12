def addBinary(a,b):
    n_a = len(a)
    n_b = len(b)
    if n_a > n_b:
        b = "0"*(n_a-n_b) + b
    else:
        a = "0"*(n_b-n_a) + a
    a = "0" + a
    b = "0" + b

    n = len(a)
    carry = 0
    idx = 0
    answer = ""

    while idx < n:
        sum = int(a[n-1-idx]) + int(b[n-1-idx]) + carry
        if sum == 3:
            answer = "1" + answer
            carry = 1
        elif sum == 2:
            answer = "0" + answer
            carry = 1
        else:
            answer = str(sum) + answer
            carry = 0
        idx += 1

    if answer[0] == "0":
        return answer[1:]
    return answer

def main():
    a = "11"
    b = "1"
    print(addBinary(a,b))

main()