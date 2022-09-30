def sort_array_by_parity(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] % 2 != 0:
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                r -= 1
        else:
            l += 1
    return nums
