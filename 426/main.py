# Convert a Binary Tree to a Circular Doubly Link List
# Given a Binary Tree, convert it to a Circular Doubly Linked List (In-Place).

# The left and right pointers in nodes are to be used as previous and next pointers respectively in converted Circular Linked List.
# The order of nodes in List must be same as Inorder of the given Binary Tree.
# The first node of Inorder traversal must be head node of the Circular List.


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BstToDLL:
    head, prev = None, None

    def do(self, root):
        if root == None:
            return

        self.inorder(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def inorder(self, cur):
        if cur is None:
            return

        self.inorder(cur.left)

        if self.head == None:
            self.head = cur
            self.prev = cur
        else:
            cur.left = self.prev
            self.prev.right = cur
            self.prev = cur

        self.inorder(cur.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    bst2dll = BstToDLL()
    head = bst2dll.do(root)
