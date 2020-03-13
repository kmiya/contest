# recursive solution not needed to serialize 'null' leaves
# input: [1,2,3,null,null,4,5]
# serializes to: 0:,1:1,2:2,3:3,6:4,7:5
# serialize() time: O(#nodes), space: O(#nodes)
# deserialize() time: O(#nodes), space: O(#nodes)

from typing import Dict


class Codec:

    def serialize(self, root: TreeNode) -> str:
        height = 1
        ret = [(0, '')]

        def rec(node: TreeNode, level: int, pos: int):
            nonlocal ret, height
            if not node:
                return
            height = max(height, level)
            ret.append((pos, str(node.val)))
            rec(node.left, level + 1, pos * 2)
            rec(node.right, level + 1, pos * 2 + 1)
        rec(root, 1, 1)
        return ','.join([str(key) + ':' + val for key, val in ret])

    def deserialize(self, data: str) -> TreeNode:
        nodes = {int(val.split(':')[0]): val.split(':')[1] for val in data.split(',')}

        def rec(pos: int, nodes: Dict[int, str]) -> TreeNode:
            if pos not in nodes or nodes[pos] == '':
                return None
            node = TreeNode(int(nodes[pos]))
            node.left = rec(2 * pos, nodes)
            node.right = rec(2 * pos + 1, nodes)
            return node

        return rec(1, nodes)
