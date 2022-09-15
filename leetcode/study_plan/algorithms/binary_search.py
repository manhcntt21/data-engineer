def binary_search(nums, l, r, t):
    if l <= r:
        m = l + (r - l) // 2
        if nums[m] == t:
            return m
        elif t < nums[m]:
            return binary_search(nums, l, m - 1, t)
        else:
            return binary_search(nums, m + 1, r, t)
    else:
        return -1
nums = [-4, -1, 0, 3, 10]
binary_search(nums, 0, 4, -4)