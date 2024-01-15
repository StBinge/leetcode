#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level=[root]
        ret=0
        s=float('-inf')
        l=1
        while level:
            temp=[]
            cur=0
            for node in level:
                cur+=node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if cur>s:
                s=cur
                ret=l
            l+=1
            level=temp
        return ret
# @lc code=end
assert Solution().maxLevelSum(TreeNode.build('[-100,-200,-300,-20,-5,-10,null]'))==3
assert Solution().maxLevelSum(TreeNode.build('[1,7,0,7,-8,null,null]'))==2
