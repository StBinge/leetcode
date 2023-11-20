#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# @lc code=start
"""
# Definition for a Node.
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        d=0
        for ch in root.children:
            d=max(d,self.maxDepth(ch))
        return 1+d
        
# @lc code=end

