class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.node_to_key = {}
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
    
    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def push(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.pop(node)
        self.push(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.pop(node)
        else:
            node = Node()
            self.key_to_node[key] = node
            self.node_to_key[node] = key
        node.val = value
        self.push(node)
        if len(self.key_to_node)>self.capacity:
            node = self.left.next
            key = self.node_to_key[node]
            self.pop(node)
            del self.key_to_node[key]
            del self.node_to_key[node]