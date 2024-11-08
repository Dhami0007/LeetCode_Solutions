def minFlips(a, b, c):
    # max limit is 10^9 so we can use 30 bits
    i = 1
    flips = 0
    for _ in range(31):
        if (c & i) == 0:
            if (a & i) != 0:
                flips += 1
            if (b & i) != 0:
                flips += 1
        else:
            if (a & i) == 0 and (b & i) == 0:
                flips += 1
        i = i << 1
    return flips

def main():
    a = 2 
    b = 6 
    c = 5
    print(minFlips(a, b, c))

main()