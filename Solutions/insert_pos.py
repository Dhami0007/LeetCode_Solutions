def insert_pos(nums,target):
    start = 0
    end = len(nums) - 1
    mid = 0
    while end-start > 1:
        mid = (start + end)//2
        print(f"mid {mid}")
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            print("returning mid")
            return mid
    print(f"start {start} end {end}")
    if nums[end] < target:
        return end + 1
    elif nums[start] < target:
        return end
    elif nums[start] > target:
        return start

def main():
    nums = [1,3,5,6]
    target = 7
    print(insert_pos(nums, target))

main()