# O(n) no pass
# def two_sum(nums, t):
#     for i in range(len(nums) - 1):
#         print(i)
#         for j in range(i + 1, len(nums)):
#             print(j)
#             if nums[i] + nums[j] == t:
#                 return [i + 1, j + 1]

# two pointer O(n)
# def two_sum(nums, t):
#     l, r = 0, len(nums) - 1
#     while l < r:
#         s = nums[l] + nums[r]
#         if s == t:
#             return [l+1, r+1]
#         elif s < t:
#             l += 1
#         else:
#             r -= 1
#     return -1
#
# numbers = [2, 3, 4]
# print(two_sum(numbers, 6))

