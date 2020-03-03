# straightforward solution
# time: O(num of nodes)
# space: O(num of nodes)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def rec(tree: TreeNode, list: List[int]):
            if not tree:
                return
            list.append(tree.val)
            rec(tree.left, list)
            rec(tree.right, list)
            return
        ret = []
        rec(root, ret)
        return ret