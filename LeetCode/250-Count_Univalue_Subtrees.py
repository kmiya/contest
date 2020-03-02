# algorithm described in Solution page (DFS)
# time: O(#nodes)
# space: O(#nodes)


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        ret = 0

        def rec(node: TreeNode, val: int) -> bool:
            if not node:
                return True
            nonlocal ret
            if not all([rec(node.left, node.val), rec(node.right, node.val)]):
                return False
            ret += 1
            return val == node.val

        if root:
            rec(root, root.val)
        return ret
