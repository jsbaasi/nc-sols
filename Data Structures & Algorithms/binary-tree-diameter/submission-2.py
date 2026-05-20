# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # post visit order
        res = 0
        def rec(root):
            nonlocal res
            if not root: return 0
            elif not root.left and not root.right: return 1
            else:
                h1, h2 = rec(root.left), rec(root.right)
                res = max(res, h1+h2)
                return max(h1,h2) + 1
        rec(root)
        return res


