# dirty iterative solution (linear space)
# time: O(#nodes)
# space: O(1)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def left_or_right(node: 'Node') -> 'Node':
            if node.left:
                return node.left
            if node.right:
                return node.right
            return None

        if not root:
            return root

        leftmost = root
        while leftmost:
            head = leftmost
            src = dst = None
            while head:
                if head.left and head.right:
                    head.left.next = head.right
                    src = head.right
                if not src:
                    src = left_or_right(head)
                    if not src:
                        head = head.next
                        continue
                if head.next:
                    dst = left_or_right(head.next)
                if dst:
                    src.next = dst
                    src, dst = dst, None
                head = head.next
            while leftmost:
                next_left = left_or_right(leftmost)
                if next_left:
                    leftmost = next_left
                    break
                leftmost = leftmost.next
        return root