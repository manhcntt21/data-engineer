def searchInsert(nums, t: int) -> int:
    return binary_search(nums, 0, len(nums) - 1, t)


def binary_search(arr, l, r, x):
    if l <= r:
        m = l + (r - l) // 2
        if arr[m] == x:
            return m
        elif x < arr[m]:
            return binary_search(arr, l, m - 1, x)
        else:
            return binary_search(arr, m + 1, r, x)
    else:
        if r < 0:
            return l + 1 if arr[l] < x else l
        else:
            return l if arr[l - 1] < x else l - 1