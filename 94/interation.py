# interative time O(n) space O(n)
# use stack to track path
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        answer = []
        self.inorderTraversalHelper(root, stack, answer)
        return answer

    def inorderTraversalHelper(self, cur, stack, answer):
        if cur is None:
            return

        while cur or len(stack) != 0:
            # left
            while cur:
                stack.append(cur)
                cur = cur.left
            # left done, do cur
            cur = stack.pop()
            answer.append(cur.val)
            # right
            cur = cur.right
