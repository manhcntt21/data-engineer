def find_disappeared_numbers(nums):
    n = len(nums)
    seen = set(nums)
    disappeared = []
    for i in range(1, n + 1):
        if i not in seen:
            disappeared.append(i)
    return disappeared
