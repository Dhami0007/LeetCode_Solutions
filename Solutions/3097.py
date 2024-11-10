def minimumSubarrayLength(nums, k):
    start = 0
    end = 0
    answer = float('inf')
    freq = [0 for _ in range(30)]
    current = 0

    while end < len(nums):
        current |= nums[end]
        addFreq(freq, nums[end])

        while start <= end and current >= k:
            answer = min(answer, end - start + 1)
            subFreq(freq, nums[start])
            current = calcNum(freq) 
            start += 1
        end += 1
    
    if answer == float('inf'):
        return -1
    return answer

def calcNum(freq):
    num = 0
    for i in range(30):
        if freq[i] > 0:
            num |= (1 << i)
    return num

def subFreq(freq, num):
    for i in range(30):
        if num & (1 << i):
            freq[i] -= 1

def addFreq(freq, num):
    for i in range(30):
        if num & (1 << i):
            freq[i] += 1


def main():
    nums = [1,2]
    k = 0
    print(minimumSubarrayLength(nums, k))

main()