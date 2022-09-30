from square_of_sorted_array import merge_sort


def height_checker(heights):
    heights_original = heights.copy()
    sorted_heights = merge_sort(heights, 0, len(heights) - 1)
    count = 0
    for i in range(len(heights)):
        if sorted_heights[i] != heights_original[i]:
            count += 1
    return count

