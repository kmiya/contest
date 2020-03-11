# recursive solution described in Solution page
# time: O(#nodes)
# space: O(#nodes)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def rec(node: 'TreeNode') -> bool:
            nonlocal lca
            if lca:
                return False
            if not node:
                return False
            mid = node.val == p.val or node.val == q.val
            left = rec(node.left)
            right = rec(node.right)
            if mid & left or mid & right or left & right:
                lca = node
            return mid or left or right

        rec(root)
        return lca
