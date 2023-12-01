#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        L=len(nums)
        stk=[]
        # left=[-1]*L
        # right=[-1]*L
        # nodes=[TreeNode(val) for val in nums]
        nodes=[None]*L
        for i in range(L):
            nodes[i]=TreeNode(nums[i])
            while stk and nums[i]>nums[stk[-1]]:
                # right[stk[-1]]=i
                nodes[i].left=nodes[stk[-1]]
                stk.pop()
            if stk:
                # left[i]=stk[-1]
                nodes[stk[-1]].right=nodes[i]
            stk.append(i)
        
        
        return nodes[stk[0]]
        
        
# @lc code=end

Solution().constructMaximumBinaryTree([3,2,1,6,0,5])