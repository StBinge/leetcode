#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
# @lc code=start
"""
# Definition for a Node.
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ret=[]
        queue=[root]
        while queue:
            temp=[]
            vals=[]
            for node in queue:
                vals.append(node.val)
                if not node.children:
                    continue
                for child in node.children:
                    temp.append(child)
            ret.append(vals)
            queue=temp
        return ret
# @lc code=end

