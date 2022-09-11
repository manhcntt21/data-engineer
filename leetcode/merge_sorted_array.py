# explain: https://leetcode.com/problems/merge-sorted-array/discuss/785646/Python-3-greater-99.78-faster
def merge(nums1, nums2, m ,n):
    # nums1.extend(nums2)
    # nums1.sort()
    # return nums1
    new_index = m + n + 1
    while m >= 0 and n >= 0:
        if nums1[m] <= nums2[n]:
            nums1[new_index] = nums2[n]
            n -= 1
        elif nums1[m] > nums2[n]:
            nums1[new_index] = nums1[m]
            m -= 1
        new_index -= 1

    if m < 0:
        nums1[0: n + 1] = nums2[0: n + 1]
    print(nums1)


merge([7, 8, 0, 0], [6, 10], 1, 1)