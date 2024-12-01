def minEatingSpeed(piles, h):
    
    def timeTaken(piles, k):
        time = 0
        for pile in piles:
            time += pile // k
            if pile % k != 0:
                time += 1
        return time

    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2 # this is to prevent overflow in case of big numbers
        time = timeTaken(piles, mid)
        if time > h:
            left = mid + 1
        else:
            right = mid
    
    return left

def main():
    piles = [30,11,23,4,20]
    h = 6

    print(minEatingSpeed(piles, h))

main()