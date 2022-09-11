# problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums):
    # solution 1
    # k = 1
    # for i in range(1, len(nums)):
    #     if nums[i] != nums[i-1]:
    #         nums[k] = nums[i]
    #         k += 1
    # print(id(nums))
    # return k, nums

    # solution 2
    # explain: [:] https://realpython.com/lessons/indexing-and-slicing/
    # [:] == shallow copy
    k = len(set(nums))
    nums[:] = list(set(nums))
    return k, nums


nums = [0, 0, 1, 1, 2]
print(remove_duplicates(nums))