def reverse_string(s):
    s[:] = s[::-1]

# two pointer appoach
def reverse_string_1(a):
    i, j = 0, len(a) - 1
    while i <= j:
        b = a[i]
        a[i] = a[j]
        a[j] = b
        i += 1
        j -= 1

