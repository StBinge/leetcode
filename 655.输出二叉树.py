#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # ret=[]
        def get_depth(root:TreeNode):
            if not root:
                return 0
            return 1+max(get_depth(root.left),get_depth(root.right))

        rows=get_depth(root)
        cols=2**rows-1
        ret=[['']*cols for _ in range(rows)]
        def build(root:TreeNode,depth,left,right):
            if not root:
                return
            center=(left+right)//2
            ret[depth][center]=str(root.val)
            build(root.left,depth+1,left,center-1)
            build(root.right,depth+1,center+1,right)
        
        build(root,0,0,cols-1)
        return ret

# @lc code=end

