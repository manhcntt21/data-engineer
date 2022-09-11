# problem: https://www.hackerrank.com/challenges/apple-and-orange/problem

def count_apple_orange(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0
    for i in range(len(apples)):
        if (apples[i] + a <= t) and (apples[i] + a >= s):
            count_apple = count_apple + 1
    for i in range(len(oranges)):
        if (oranges[i] + b <= t) and (oranges[i] + b >= s):
                count_orange = count_orange + 1

    print(count_apple, count_orange)


if __name__ == '__main__':
    with open('input/count_apple_orange.txt', encoding='utf-8') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    s, t = [int(i)for i in data[0].split(' ')]
    a, b = [int(i)for i in data[1].split(' ')]
    apples = [int(i)for i in data[3].split(' ')]
    oranges = [int(i)for i in data[4].split(' ')]

    count_apple_orange(s, t, a, b, apples, oranges)