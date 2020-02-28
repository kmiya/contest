# straightforward recursive solution
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []

        def rec(node: TreeNode, level: int):
            if len(ret) == level:
                ret.append([])
            if not node:
                return
            ret[level].append(node.val)
            if node.left:
                rec(node.left, level + 1)
            if node.right:
                rec(node.right, level + 1)
            return

        rec(root, 0)
        return ret
