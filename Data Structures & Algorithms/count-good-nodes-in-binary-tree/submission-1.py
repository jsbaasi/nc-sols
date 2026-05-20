# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path = []
        res = 1
        def dfs(root):
            if not root: return
            nonlocal res
            if root.val >= max(path, default=float("inf")): res+=1
            path.append(root.val)
            dfs(root.left)
            dfs(root.right)
            path.pop()
            return
        dfs(root)
        return res