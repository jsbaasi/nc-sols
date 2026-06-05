# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def rec(node):
            if not node: return ["None"]
            else: return [str(node.val)] + rec(node.left) + rec(node.right)
        array = rec(root)
        return ",".join(array)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(",")
        def rec(i):
            if array[i]=="None": return (None, i+1)
            root = TreeNode(int(array[i]))
            root.left, j = rec(i+1)
            root.right, k = rec(j)
            return (root, k)
        root, _ = rec(0)
        return root


