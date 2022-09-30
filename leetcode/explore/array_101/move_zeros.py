def move_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(nums.index(nums[i])))
    print(nums)
