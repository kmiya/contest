# dirty and not memory efficient solution
# preserves all common ancestors
# time: O(#nodes * log(#nodes))
# space: O(#nodes^2)

import copy
from typing import List


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not (root.left or root.right):
            return root

        path_p = path_q = []
        dic = {}

        def rec(node: 'TreeNode', path: List, level: int):
            nonlocal path_p, path_q, p, q
            if (path_p and path_q) or not node:
                return
            dic[node.val] = node
            path.append((level, node.val))
            if node.val == p.val:
                path_p = copy.deepcopy(path)
            elif node.val == q.val:
                path_q = copy.deepcopy(path)
            if not (node.left or node.right):
                path.pop()
                return
            rec(node.right, path, level + 1)
            rec(node.left, path, level + 1)
            if path:
                path.pop()

        rec(root, [], 0)
        commons = set(path_p) & set(path_q)
        return dic[list(sorted(commons))[-1][1]]
