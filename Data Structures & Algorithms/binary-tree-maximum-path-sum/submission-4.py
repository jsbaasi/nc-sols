# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def rec(root):
            if not root: return 0
            nonlocal res
            l = max(rec(root.left), 0)
            r = max(rec(root.right), 0)
            res = max(res, l+root.val+r)
            return max(l+root.val, root.val+r, 0)
        rec(root)
        return res