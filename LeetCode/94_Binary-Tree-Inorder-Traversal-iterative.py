# iterative solution
# time: O(n)
# space: O(n)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ret = []
        node = root
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ret.append(node.val)
            node = node.right
        return ret
