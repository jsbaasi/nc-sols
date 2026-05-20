# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        def rec(root):
            nonlocal is_balanced
            if not root: return 0
            elif not root.left and not root.right: return 1
            else:
                h1, h2 = rec(root.left), rec(root.right)
                if abs(h1-h2)>1: is_balanced = False
                return max(h1,h2) + 1
        rec(root)
        return is_balanced
