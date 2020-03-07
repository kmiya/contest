# recursive solution with stack
# time: O(#nodes)
# space: O(#nodes)


class Solution:
    def rec(self, node: TreeNode, direction: str, depth: int) -> int:
        if not node:
            return depth
        if direction == 'left':
            if not node.left:
                return depth
            node, direction = node.left, 'right'
        else:
            if not node.right:
                return depth
            node, direction = node.right, 'left'
        depth += 1
        return self.rec(node, direction, depth)

    def longestZigZag(self, root: TreeNode) -> int:
        ans = 0
        if not root:
            return ans
        stack = [(root, None)]
        while len(stack):
            node, direction = stack.pop()
            if not node:
                continue
            if direction == 'left':
                ans = max(ans, self.rec(node, 'left', 0))
            if direction == 'right':
                ans = max(ans, self.rec(node, 'right', 0))
            if not direction:
                ans = max(ans, self.rec(node, 'left', 0))
                ans = max(ans, self.rec(node, 'right', 0))
            stack.append((node.left, 'left'))
            stack.append((node.right, 'right'))
        return ans
