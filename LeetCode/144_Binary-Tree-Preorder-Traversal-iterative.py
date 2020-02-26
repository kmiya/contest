# iterative solution using stack
# time: O(num of nodes)
# space: O(num of nodes)

 class Solution:   
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        node = root
        stack = []
        ret = []
        while True:
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not len(stack):
                break
            node = stack.pop()
        return ret