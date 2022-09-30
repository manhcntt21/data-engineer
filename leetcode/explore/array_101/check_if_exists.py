def check_if_exist1(arr):
    seen = set()
    for i in arr:
        if i * 2 in seen or i / 2 in seen: return True
        seen.add(i)
    return False


def check_if_exits2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]*2 and i != j:
                return True
    return False
