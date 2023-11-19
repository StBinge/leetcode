#
# @lc app=leetcode.cn id=558 lang=python3
#
# [558] 四叉树交集
#
from quadnode import QuadNode as Node
# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True,True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2,quadTree1)

        topLeft=self.intersect(quadTree1.topLeft,quadTree2.topLeft)
        topRight=self.intersect(quadTree1.topRight,quadTree2.topRight)
        bottomLeft=self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
        bottomRight=self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val==topRight.val==bottomLeft.val==bottomRight.val:
            return Node(topLeft.val,isLeaf=True)
        else:
            return Node(False,False,topLeft=topLeft,topRight=topRight,bottomLeft=bottomLeft,bottomRight=bottomRight)
# @lc code=end

root1=Node.build([[0,1],[1,1],[1,1],[1,0],[1,0]])
root2=Node.build('[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]')
ret=Solution().intersect(root1,root2)
pass