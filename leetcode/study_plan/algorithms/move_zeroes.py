def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.append(nums.pop(nums.index(nums[i])))
    print(nums)

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)