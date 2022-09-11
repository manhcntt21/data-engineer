# problem: https://www.hackerrank.com/challenges/mini-max-sum/problem

def min_max_sum(array):
    array.sort()
    print(sum(array[1:]), sum(array[:-1]))


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    min_max_sum(array)