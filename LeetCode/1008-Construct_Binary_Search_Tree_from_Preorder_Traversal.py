# Time: O(N log N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def rec(node, i):
            if not node:
                return TreeNode(i)
            if i < node.val:
                if not node.left:
                    node.left = TreeNode(i)
                else:
                    node.left = rec(node.left, i)
            if i > node.val:
                if not node.right:
                    node.right = TreeNode(i)
                else:
                    node.right = rec(node.right, i)
            return node

        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            root = rec(root, i)

        return root