# iterative solution using stack
# time: O(num of nodes)
# space: O(num of nodes)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root.left, root.right)]
        while len(stack):
            l, r = stack.pop()
            if not (l or r): continue
            if not (l and r): return False
            if l.val != r.val: return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
