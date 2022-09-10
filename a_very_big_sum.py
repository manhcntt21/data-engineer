# problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true

def a_very_big_sum(ar):
    """
    return: the sum of all array elements
    """
    big_sum = 0
    return sum(ar)


if __name__ == '__main__':
    with open('./input/a_very_big_sum.txt', encoding='utf-8') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    n = data[0]
    array = data[1].split(' ')
    array = [int(x) for x in array]
    result = a_very_big_sum(array)

    # write result to file
    # str_array = ", ".join(array)

    with open('./input/a_very_big_sum_out.txt', 'w') as f:
        f.write(str(result))

