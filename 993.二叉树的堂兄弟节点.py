#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        dx=-1,-1
        dy=-1,-1
        def traverse(node:TreeNode,d:int,p:int):
            nonlocal dx,dy
            if not node:
                return
            if node.val==x:
                dx=d,p
            if node.val==y:
                dy=d,p
            traverse(node.left,d+1,node.val)
            traverse(node.right,d+1,node.val)
        traverse(root,0,-1)
        return dx[0]==dy[0] and dx[1]!=dy[1]
# @lc code=end
root = '[1,2,3,null,4,null,5]'
x = 2
y = 3
assert not Solution().isCousins(TreeNode.build(root),x,y)
root = '[1,2,3,null,4,null,5]'
x = 5
y = 4
assert Solution().isCousins(TreeNode.build(root),x,y)

root = [1,2,3,4]
x = 4
y = 3
assert not Solution().isCousins(TreeNode.build(root),x,y)
