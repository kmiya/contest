# straightforward recursive solution
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ret = []
        ret.extend(self.postorderTraversal(root.left))
        ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret
