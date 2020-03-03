# straightforward recursive solution
# time: O(n)
# space: O(n)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        if root.left:
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right:
            ret.extend(self.inorderTraversal(root.right))
        return ret
