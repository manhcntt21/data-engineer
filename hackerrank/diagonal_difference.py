# problem: https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def diagonal_differences(array, n):
    """
        principal same index
        secondary i + j = n -1
        time complexity: O(n)
    :param array:
    :type array:
    :param n:
    :type n:
    :return:
    :rtype:
    """
    principal_diagonal = 0
    secondary_diagonal = 0
    for i in range(n):
        principal_diagonal += array[i][i]
        secondary_diagonal += array[i][n-i-1]
    return abs(principal_diagonal - secondary_diagonal)


if __name__ == '__main__':
    with open('input/diagonal_differences.txt', encoding='utf-8') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    n = int(data[0])
    array = data[1:]
    array = [[int(j) for j in i.split(' ')] for i in array]
    # arr = [for row in data]
    result = diagonal_differences(array, n)
    with open('input/diagonal_differences_out.txt', 'w') as f:
        f.write(str(result))