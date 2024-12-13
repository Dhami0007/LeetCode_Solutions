def getMaximumXor(nums, maximumBit):
    xor = 0
    max = (1 << maximumBit) - 1
    answer = list()

    for num in nums:
        xor ^= num
        answer.append(max ^ xor)
    
    return answer[::-1]

def main():
    nums = [0,1,1,3]
    maximumBit = 2
    print(getMaximumXor(nums, maximumBit))

main()