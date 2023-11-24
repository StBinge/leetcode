#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def make(i,j,k):
            if k==0:
                return None
            root=TreeNode(preorder[i])
            if k==1:
                return root
            kk=postorder.index(preorder[i+1],j)-j+1
            root.left=make(i+1,j,kk)
            root.right=make(i+1+kk,j+kk,k-kk-1)
            return root

        return make(0,0,len(preorder))
# @lc code=end
preorder = [2,1]
postorder = [1,2]
Solution().constructFromPrePost(preorder,postorder).print()

preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
Solution().constructFromPrePost(preorder,postorder).print()

preorder = [1]
postorder = [1]
Solution().constructFromPrePost(preorder,postorder).print()
