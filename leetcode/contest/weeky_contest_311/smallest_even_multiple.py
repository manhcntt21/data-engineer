def uscln(a, b):
    if b == 0:
        return a
    else:
        return uscln(b, a % b)


def bscnn(a, b):
    return int((a * b) / uscln(a, b))


print(bscnn(6, 2))
