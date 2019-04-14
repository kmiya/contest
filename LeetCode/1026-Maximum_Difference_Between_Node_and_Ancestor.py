# time: O(n)
# space: O(1)
# Runtime: 48 ms, faster than 100.00% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def rec(node, max_i, min_i):
            if not node:
                return abs(max_i - min_i);
            arg_max, arg_min = max_i, min_i
            if node.val > max_i:
                arg_max, arg_min = node.val, min_i
            elif node.val < min_i:
                arg_max, arg_min = max_i, node.val
            labs = rec(node.left, arg_max, arg_min)
            rabs = rec(node.right, arg_max, arg_min)
            return labs if labs > rabs else rabs
        return rec(root, root.val, root.val)