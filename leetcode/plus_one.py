import functools


def plus_one(digits):
    s = ''.join([str(i) for i in digits])
    number = int(s) + 1
    s = str(number)
    res = [int(x) for x in str(number)]
    return res


    # return [x for x in str(int(''.join(map(str, digits))) + 1)]


if __name__ == '__main__':
    print(plus_one([1, 0, 0, 0]))