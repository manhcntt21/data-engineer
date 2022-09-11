# problem: https://leetcode.com/problems/palindrome-number/
# explain, why 0(logn) https://stackoverflow.com/questions/50261364/explain-why-time-complexity-for-summing-digits-in-a-number-of-length-n-is-ologn
def palindrome_numb(x):
    if x % 10 == 0:
        return False
    else:
        orig = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return orig == back_x


if __name__ == '__main__':
    print(palindrome_numb(-121))