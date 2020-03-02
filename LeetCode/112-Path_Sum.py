# straightforward recursive solution
# time: O(#nodes)
# space: O(#nodes)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def rec(node: TreeNode, num: int) -> bool:
            if not node:
                return False
            num += node.val
            if not (node.left or node.right):  # leaf
                if num == sum:
                    return True
                return False
            return rec(node.left, num) or rec(node.right, num)
        return rec(root, 0)
