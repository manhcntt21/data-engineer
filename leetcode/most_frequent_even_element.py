import operator
nums = [0, 0, 0, 0]


def solution():
    nums_dict = {i: nums.count(i) for i in nums if i % 2 == 0}
    if nums_dict != {}:
        max_value = max(nums_dict.items(), key=operator.itemgetter(1))[1]
        nums_dict = {k: v for (k, v) in nums_dict.items() if v == max_value}
        return min(nums_dict.items(), key=operator.itemgetter(0))[0]
    else:
        return -1


print(solution())