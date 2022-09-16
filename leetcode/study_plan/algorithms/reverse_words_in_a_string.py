import functools
s = "Let's take LeetCode contest"

def reverse_string_1(a):
    i, j = 0, len(a) - 1
    while i <= j:
        b = a[i]
        a[i] = a[j]
        a[j] = b
        i += 1
        j -= 1
    return a

def reverse_words(s):
    s = s.split(' ')
    s = [''.join(reverse_string_1(list(i))) for i in s]
    return ' '.join(s)
print(reverse_words(s))


