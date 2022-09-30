def find_max_consecutive_ones(nums):
    count = max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(count, max_count)
