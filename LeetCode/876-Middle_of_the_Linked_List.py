# double pointer
# time: O(N)
# time: O(1)


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        node = middle = head
        flipflop = False
        while node:
            if flipflop:
                middle = middle.next
            flipflop = not flipflop
            node = node.next
        return middle
