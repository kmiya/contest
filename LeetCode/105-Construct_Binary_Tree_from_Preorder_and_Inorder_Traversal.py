# same as Problem 106
# time: O(#nodes)
# time: O(#nodes)


from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def rec(left: int, right: int) -> TreeNode:
            nonlocal preIdx
            if left > right:
                return None
            root = TreeNode(preorder[preIdx])
            preIdx += 1
            mid = dic[root.val]
            root.left = rec(left, mid - 1)
            root.right = rec(mid + 1, right)
            return root
        preIdx = 0
        dic = {num: idx for idx, num in enumerate(inorder)}
        return rec(0, len(inorder) - 1)
