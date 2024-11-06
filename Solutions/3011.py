# This set bits function is taken from https://www.sanfoundry.com/python-program-count-set-bits-number/
def setBits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def canSortArray(nums):
    max_mins = list()
    startBits = setBits(nums[0])
    max = 0
    min = float('inf')

    for num in nums:    
        bits = setBits(num)
        if bits == startBits:
            if num > max:
                max = num
            if num < min:
                min = num
        else:
            max_mins.append((max, min))
            startBits = bits
            max = num
            min = num

    max_mins.append((max, min))

    output = True
    i = 0
    while i < len(max_mins) - 1:
        if max_mins[i][0] > max_mins[i+1][1] or max_mins[i][1] > max_mins[i+1][0]:
            output = False
        i += 1
    
    return output

def main():
    # The submission passed all the cases
    nums = [8,4,2,30,15]
    print(canSortArray(nums))

main()