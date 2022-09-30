def max_consecutive_ii(nums):
    dp1 = [0]*len(nums)
    dp2 = [0]*len(nums)
    ans = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            dp1[i] = 0
            dp2[i] = 1 if i < 1 else dp1[i-1] + 1
        else:
            dp1[i] = 1 if i < 1 else dp1[i-1] + 1
            dp2[i] = 1 if i < 1 else dp2[i-1] + 1
        ans = max(ans, dp2[i])
    print(ans)


if __name__ == '__main__':
    numbers = [1, 1, 1, 0, 1, 1, 0, 1, 1]
    max_consecutive_ii(nums=numbers)
