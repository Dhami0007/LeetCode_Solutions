import heapq

def findKthLargest(nums, k):
    # we can use min heap from heapq to solve this problem

    min_heap = nums[:k]
    heapq.heapify(min_heap)

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappush(min_heap, nums[i])
            heapq.heappop(min_heap)
    return min_heap[0]

def main():
    nums = [3,2,1,5,6,4]
    k = 2
    print(findKthLargest(nums, k))

main()
