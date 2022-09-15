#solution 1
def rotate1(nums, k):
    n = len(nums)
    nums[:] = [nums[(n - k + i) % n] for i in range(0, n)]
    print(nums)

# solution 2
# 1. reverse the first n - k elements
# 2. reverse the rest of them
# 3. reverse the entire array
def rotate2(nums, k):
    n = len(nums)
    nums[n - k%n:n] = nums[n - k%n:n][::-1]
    nums[:n - k%n] = nums[:n - k%n][::-1]
    nums[:] = nums[::-1]
    print(nums)

k = 5
nums = [1, 2]
rotate1(nums, k)
nums = [1, 2]
rotate2(nums, k)
# print(nums)
# print(nums[2:4])