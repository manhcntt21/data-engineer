def valid_mountain_array(arr):
    flag1 = -1
    flag2 = -1
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            flag1 = i
            break

    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] <= arr[i]:
            flag2 = i
            break

    if flag1 == flag2 and flag1 != -1:
        return True
    return False
