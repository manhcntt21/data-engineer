def binary_search(self, nums, l, r, t):
    if l <= r:
        m = l + (r - l) // 2
        if nums[m] == t:
            return m
        elif t < nums[m]:
            return self.binary_search(nums, l, m - 1, t)
        else:
            return self.binary_search(nums, m + 1, r, t)
    else:
        return -1