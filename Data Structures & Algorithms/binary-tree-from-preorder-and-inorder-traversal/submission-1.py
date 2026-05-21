# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        pre := root, left, right
        inorder := left, root, right
        we're at a root, we can assume the node is good to go
        then we recursively call the other nodes
        """
        taken = set()
        n = len(preorder)

        def dfs(root, i, p):
            left_values = set()
            for j in range(i-1, -1, -1): 
                if inorder[j] in taken: break
                left_values.add(inorder[j])
            right_values = set()
            for j in range(i+1, n):
                if inorder[j] in taken: break
                right_values.add(inorder[j])
            l_i_p = None
            r_i_p = None
            if left_values:
                for j in range(p + 1, n):
                    if preorder[j] in taken: break
                    if preorder[j] in left_values and preorder[j] not in taken:
                        taken.add(preorder[j])
                        l_i_p = (inorder.index(preorder[j]), j)
                        break
            if right_values:
                for j in range(p + 1, n):
                    if preorder[j] in right_values and preorder[j] not in taken:
                        taken.add(preorder[j])
                        r_i_p = (inorder.index(preorder[j]), j)
                        break
            root.left = dfs(TreeNode(preorder[l_i_p[1]]), l_i_p[0], l_i_p[1]) if l_i_p else None
            root.right = dfs(TreeNode(preorder[r_i_p[1]]), r_i_p[0], r_i_p[1]) if r_i_p else None
            return root
        taken.add(preorder[0])
        return dfs(TreeNode(preorder[0]), inorder.index(preorder[0]), 0)
