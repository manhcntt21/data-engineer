def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0]*n1
    R = [0]*n2

    # copy data to temp arrays L, R
    for i in range(0, n1):
        L[i] = a[l + i]
    for j in range(0, n2):
        R[j] = a[m + j + 1]

    # merge two temp arrays back to a
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # copy remaining element of L[R], if there are
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


def merge_sort(a, l, r):
    if l < r:
        m = l + (r-l)//2
        merge_sort(a, l, m)
        merge_sort(a, m + 1, r)
        merge(a, l, m, r)


def solution(nums, l, r):
    squares = [i*i for i in nums]
    merge_sort(squares, l, r)


nums = [-4, -1, 0, 3, 10]
solution(nums, 0, 4)
print(nums)
