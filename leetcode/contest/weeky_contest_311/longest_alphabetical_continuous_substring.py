def get_ending_index(str1, n, i):
    i += 1
    while i < n:

        curr = str1[i]
        prev = str1[i - 1]

        # If the current character appears after
        # the previous character according to
        # the given circular alphabetical order
        if (ord(curr) - ord(prev)) == 1:
            i += 1
        else:
            break

    return i - 1


def largest_substr1(str1, n):
    _len = 0
    i = 0
    while (i < n):
        # Valid sub-string exists from
        # index i to end
        end = get_ending_index(str1, n, i)
        # Update the Length
        _len = max(end - i + 1, _len)
        i = end + 1
    return _len


word = "zabwwg"
print(largest_substr1(word, len(word)))
