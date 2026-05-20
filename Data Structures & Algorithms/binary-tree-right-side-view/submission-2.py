# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, level):
            if not root: return False
            if len(res)<level: res.append(root.val)
            if not dfs(root.right, level+1):
                if not dfs(root.left, level+1):
                    return False
            return True
        dfs(root, 1)
        return res