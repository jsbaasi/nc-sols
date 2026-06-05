class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def rec(node):
            if not node: return ["N"]
            else: return [str(node.val)] + rec(node.left) + rec(node.right)
        return ",".join(rec(root))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(",")
        def rec(i):
            if array[i]=="N": return (None, i+1)
            root = TreeNode(int(array[i]))
            root.left, j = rec(i+1)
            root.right, k = rec(j)
            return (root, k)
        root, _ = rec(0)
        return root