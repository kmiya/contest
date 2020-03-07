# solution described in Solution page
# time: O(#nodes)
# space: O(1)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost:
            if not leftmost.left:
                return root
            head = leftmost
            while head:
                head.left.next = head.right
                if not head.next:
                    break
                head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
