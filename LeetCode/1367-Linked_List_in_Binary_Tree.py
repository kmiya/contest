# traverse tree iteratively and match list recursively
# time: O(len(nodes) * len(head))
# space: O(len(nodes))


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def rec(head: ListNode, node: TreeNode) -> bool:
            if not (head and node):
                return False
            if not head.next and head.val == node.val:
                return True
            if head.val == node.val:
                return rec(head.next, node.left) or rec(head.next, node.right)
            return False

        stack = [root]
        while len(stack):
            node = stack.pop()
            if node.val == head.val:
                if rec(head, node):
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False
