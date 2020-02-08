# Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive time O(n) space O(n)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        self.inorderTraversalHelper(root, answer)
        return answer

    def inorderTraversalHelper(self, root, answer):
        if root is None:
            return

        self.inorderTraversalHelper(root.left, answer)
        answer.append(root.val)
        self.inorderTraversalHelper(root.right, answer)
