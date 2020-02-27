# Algorithm explained in Solution page
# traverse in top->right->left order and reverse the result
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        ret = []
        while len(stack):
            node = stack.pop()
            ret.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ret[::-1]
