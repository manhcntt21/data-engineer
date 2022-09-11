# O(n)
def search_insert(nums, t):
    if t in nums:
        return nums.index(t)
    else:
        for i in range(len(nums))[::-1]:
            if t > nums[i]:
                return i + 1
        return 0

# O(logn)
def binary_search(arr, l, r, x):
    if l <= r:
        m = l + (r - l)//2
        if arr[m] == x:
            return m;
        elif x < arr[m]: return binary_search(arr, l, m-1, x)
        else: return binary_search(arr, m + 1, r, x)
    else:
        return l + 1 if arr[l] < x else l

if __name__ == '__main__':
    print(search_insert([1, 3, 5, 6], 0))
    print(binary_search([1, 3, 5, 6], 0, 3, 5))