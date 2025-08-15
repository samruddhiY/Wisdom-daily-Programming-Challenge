def sort_arr_012(nums):
    n = len(nums)
    low, mid, high = 0, 0, n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

nums = list(map(int, input("Enter numbers (0, 1, 2) separated by spaces or commas: ").replace(",", " ").split()))

sort_arr_012(nums)
print("Sorted colors:", nums)
