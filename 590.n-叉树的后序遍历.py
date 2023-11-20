#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Definition for a Node.
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ret=[]
        if not root:
            return ret
        stack=[root]
        vis=set()
        while stack:
            node=stack[-1]
            if not node.children or len(node.children)==0 or node in vis:
                ret.append(node.val)
                stack.pop()
                continue
            stack.extend(reversed(node.children))
            vis.add(node)
        return ret
# @lc code=end
root=Node(1,children=[
    Node(3,children=[
        Node(5),
        Node(6)
    ]),
    Node(2),
    Node(4)
])
assert Solution().postorder(root)==[5,6,3,2,4,1]
