def getMaximumXor(nums, maximumBit):
    xor = 0 # This is to initialize the xor value. 0 xor any number is the number itself.
    for num in nums:
        xor ^= num
    n = len(nums)
    # we now have xor of all the numbers in the list.
    answer = list()
    i = 0
    # we will perform the query now
    # This is because 2 ** maximumBit - 1 will give us number with all the bits being 1
    # after the maximumBit + 1 position. For example, if maximumBit is 3, then 2 ** 3 - 1 = 7
    # which is 0111 in binary, where 4th bit is 0.
    # XORing this with our original xor will give us set the bits as 1 where the xor was 0, and 0 where the xor was 1.
    # This will give us the maximum possible value.
    while i < n:
        print(xor)
        answer.append(xor ^ ((2 ** maximumBit) -1))
        xor ^= nums[(n-1) - i] # this will remove the last number from xor
        i += 1 
        
    return answer

def main():
    nums = [0,1,1,3]
    maximumBit = 2
    print(getMaximumXor(nums, maximumBit))

main()