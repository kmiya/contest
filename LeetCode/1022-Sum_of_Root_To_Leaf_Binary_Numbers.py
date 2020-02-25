# time: O(t)
# time: O(h) : h is the height of t
# Runtime: 52 ms, faster than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        m = 10**9 + 7
        def rec(node, num):
            num = num + str(node.val)
            left = 0
            right = 0
            if node.left:
                left = rec(node.left, num)
            if node.right:
                right = rec(node.right, num)
            if not node.left and not node.right:
                return int(num, 2) % m
            return (left + right) % m
        return rec(root,'0')