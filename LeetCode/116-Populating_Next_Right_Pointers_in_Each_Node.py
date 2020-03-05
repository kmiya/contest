# straightforward recursive solution
# time: O(#nodes)
# space: O(#nodes)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def rec(left: 'Node', right: 'Node'):
            if not left:
                return
            left.next = right
            rec(left.left, left.right)
            rec(left.right, right.left)
            rec(right.left, right.right)
            return
        if not root:
            return root
        rec(root.left, root.right)
        return root
