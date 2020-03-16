# Time: O(n) recursive solution
# Space: O(h), where h is the height of the tree
# Runtime: 400 ms, faster than 84.16% of Python3 online submissions for Longest Univalue Path.
# Memory Usage: 17.1 MB, less than 5.45% of Python3 online submissions for Longest Univalue Path.


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        same, max_num = self.rec(root, 0)
        return max(same, max_num)

    def rec(self, root, same) -> (int, int):
        if not root:
            return 0, 0

        if not root.left and not root.right:
            return 0, 0

        sum_l = sum_r = 0
        max_num_l = max_num_r = 0

        if root.left:
            sum_l, max_num_l = self.rec(root.left, same)

        if root.right:
            sum_r, max_num_r = self.rec(root.right, same)

        max_num = max(max_num_l, max_num_r)

        if root.left and root.right:
            if root.val == root.left.val == root.right.val:
                sums = sum_l + sum_r + 2
                return max(sum_l, sum_r) + 1, max(sums, max_num)

        if root.left and root.val == root.left.val:
            return sum_l + 1, max(sum_l + 1, max_num)

        if root.right and root.val == root.right.val:
            return sum_r + 1, max(sum_r + 1, max_num)

        return 0, max_num
