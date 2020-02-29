# recursive solution
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def rec(ltree, rtree) -> bool:
            if not (ltree or rtree):
                return True
            if not (ltree and rtree):
                return False
            return ltree.val == rtree.val \
                and rec(ltree.left, rtree.right) \
                and rec(ltree.right, rtree.left)

        if not root:
            return True
        return rec(root.left, root.right)
