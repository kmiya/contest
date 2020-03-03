# algorithm described in Solution page
# time: O(#nodes)
# space: O(#nodes)


from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def rec(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            mid = dic[root.val]
            root.right = rec(mid + 1, right)
            root.left = rec(left, mid - 1)
            return root
        dic = {num: idx for idx, num in enumerate(inorder)}
        return rec(0, len(inorder) - 1)
