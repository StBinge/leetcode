#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ret=0
        def travers(node:TreeNode,least:int,most:int):
            nonlocal ret
            if not node:
                return
            # if least!=10**5:
            #     ret=max(ret,abs(least-node.val))
            # if most!=-1:
            #     ret=max(ret,abs(most-node.val))
            ret=max(ret,abs(least-node.val),abs(most-node.val))
            least=min(least,node.val)
            most=max(most,node.val)
            travers(node.left,least,most)
            travers(node.right,least,most)
        travers(root,root.val,root.val)
        return ret
# @lc code=end
assert Solution().maxAncestorDiff(TreeNode.build('[8,3,10,1,6,null,14,null,null,4,7,13]'))==7
assert Solution().maxAncestorDiff(TreeNode.build('[1,null,2,null,0,3]'))==3
