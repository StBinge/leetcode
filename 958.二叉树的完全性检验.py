#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([[root,1]])
        pre=0
        while q:
            node,idx=q.popleft()
            if pre+1!=idx:
                return False
            pre=idx
            
            if node.left:
                q.append([node.left,idx*2])
            if node.right:
                if not node.left:
                    return False
                q.append([node.right,idx*2+1])
        return True
# @lc code=end
root=TreeNode.build('[1,2,3,4,5,null,7]')
assert Solution().isCompleteTree(root)==False

root=TreeNode.build('[1,2,3,4,5,6]')
assert Solution().isCompleteTree(root)
