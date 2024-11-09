def minEnd(n, x):
    bin_x = list(bin(x)[2:])
    bin_v = list(bin(n-1)[2:])
    answer = list()

    while len(bin_v) != 0 or len(bin_x) != 0:
        if len(bin_x) == 0:
            answer.append(bin_v.pop())
        elif len(bin_v) == 0:
            answer.append(bin_x.pop())
        elif bin_x[-1] == '1':
            answer.append(bin_x.pop())
        else:
            answer.append(bin_v.pop())
            bin_x.pop()


    return int(''.join(answer[::-1]), 2)

def main():
    n = 3
    x = 1
    print(minEnd(n, x))

main()