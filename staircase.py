# problem: https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

def staircase(n):
    str = ""
    # solution 1 O(n2)
    # for i in range(n):
    #     if i == n - 1:
    #         for k in range(n):
    #             print('#', end='')
    #             str += '#'
    #     else:
    #         for j in range(n - i - 1):
    #             print(' ', end='')
    #             str += ' '
    #         for j in range(i + 1):
    #             print('#', end='')
    #             str += '#'
    #         print()
    #         str += '\n'

    # solution 2 0(n)
    # for i in range(1, n + 1):
    #     print('{}{}'.format(" " * (n - i), "#" * i))

    # solution 3
    # for i in range(1, n + 1):
    #     str += '#'
    #     print(str.rjust(n))

    # or
    # for i in range(1, n + 1):
    #     str = '#'*i
    #     print(str.rjust(n))

    # or
    for i in range(1, n + 1):
        print('{:>{x}}'.format('#'*i, x=n))
    return str


if __name__ == '__main__':
    with open('./input/staircase.txt', encoding='utf-8') as f:
        data = f.readlines()
    n = int(data[0])
    result = staircase(n)
    with open('./input/staircase_out.txt', 'w') as f:
        f.write(result)

