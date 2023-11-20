#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node:TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        
        if not root1 and not root2:
            return True
        return list(dfs(root1))==list(dfs(root2))
# @lc code=end
root1 = '[3,5,1,6,2,9,8,null,null,7,4]'
root2 = '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
root1=TreeNode.build(root1)
root2=TreeNode.build(root2)
assert Solution().leafSimilar(root1,root2)
