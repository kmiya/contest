# iterative solution
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        ret = 0
        while len(stack):
            node, level = stack.pop()
            ret = max(ret, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return ret
