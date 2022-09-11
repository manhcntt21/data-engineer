# problem: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# explain: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/2406277/Python-oror-Easily-Understood-oror-Faster-than-86-oror-Less-than-83-oror-Recursion
# code reference: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/2404416/Daily-LeetCoding-Challenge-August-Day-10
# complexity time O(nlogn) https://stackoverflow.com/questions/10324830/how-to-get-onlogn-from-tn-2tn-2-on

class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sorted_array_to_bst(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sorted_array_to_bst(nums[:mid])
        root.right = self.sorted_array_to_bst(nums[mid + 1:])
        return root


def pre_order(node):
    if node is None:
        return
    pre_order(node.left)
    print(node.val)
    pre_order(node.right)


nums = [-10, -3, 0, 5, 9]
s = Solution()
r = s.sorted_array_to_bst(nums)
pre_order(r)