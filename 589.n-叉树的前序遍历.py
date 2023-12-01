#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start
"""
# Definition for a Node.
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ret = []
        if not root:
            return ret
        stack = [root]
        while stack:
            cur = stack.pop()
            ret.append(cur.val)
            stack.extend(reversed(cur.children))
        return ret

# @lc code=end
