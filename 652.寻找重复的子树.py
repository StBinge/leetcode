#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
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
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
     
        def dfs(root:TreeNode):
            if not root:
                return ""
            serial=f'{root.val}({dfs(root.left)})({dfs(root.right)})'
            if serial in seen:
                index,node=seen[serial]
                ret.add(node)
                return '$'+str(index)
            nonlocal idx
            idx+=1
            seen[serial]=[idx,root]
            return '$'+str(idx)
            
        idx=0
        seen={}
        ret=set()
        dfs(root)
        return list(ret)
# @lc code=end

