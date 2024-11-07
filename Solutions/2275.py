def largestCombination(candidates):
    bit_list = [0 for _ in range(24)]   # This is because Hint says that there are max 24 bits in each candidate (number)
    max = 0
    for num in candidates:
        binary = bin(num)[2:]  # Convert the number to binary and remove the '0b' prefix
        n = len(binary)
        idx = 0
        while idx < n:
            if binary[(n-1)-idx] == '1':
                bit_list[idx] += 1
                if max < bit_list[idx]:
                    max = bit_list[idx]
            idx += 1
    
    # Now we have the count of 1s in each bit position
    # we need to return the max number.
    return max

def main():
    # To try Test cases
    candidates = [16,17,71,62,12,24,14]
    print(largestCombination(candidates))

main()