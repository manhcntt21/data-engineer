def third_max(nums):
    nums = sorted(list(set(nums)))
    n = len(nums)
    if n < 3:
        return max(nums)
    else:
        nums = list(nums)
        return nums[n - 3]
