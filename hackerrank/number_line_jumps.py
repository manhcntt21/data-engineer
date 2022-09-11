# problem: https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# eplain algorithms: https://www.youtube.com/watch?v=p7VdEQO16qg&ab_channel=KindsonTheTechPro
def kangaroo(x1, v1, x2, v2):
    if (x2 > x1) and (v2 > v1):
        return 'NO'
    else:
        initial_distance = x2 - x1
        velocity_diff = v1 - v2
        if initial_distance % velocity_diff == 0:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    x1, v1, x2, v2 = 0, 3, 4, 2
    kangaroo(x1, v1, x2, v2)