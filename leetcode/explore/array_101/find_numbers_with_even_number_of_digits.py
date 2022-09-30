def number_digits(number):
    if number < 10:
        return 1
    return 1 + number_digits(number // 10)


def find_numbers(nums):
    count = 0
    for i in nums:
        if number_digits(i)%2 == 0:
            count += 1
    return count
