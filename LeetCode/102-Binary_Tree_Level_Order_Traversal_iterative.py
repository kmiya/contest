# FIFO queue solution
# time: O(num of nodes)
# space: O(num of nodes)


import queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ret = []
        tmp = []
        level = 0
        q = queue.Queue()
        q.put((level, root))
        while not q.empty():
            l, node = q.get()
            if level != l:
                ret.append(tmp)
                tmp = []
                level = l
            tmp.append(node.val)
            if node.left:
                q.put((l+1, node.left))
            if node.right:
                q.put((l+1, node.right))
        ret.append(tmp)
        return ret
