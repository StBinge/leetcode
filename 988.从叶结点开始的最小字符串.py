#
# @lc app=leetcode.cn id=988 lang=python3
#
# [988] 从叶结点开始的最小字符串
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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        ret='~'
        def traverse(node:TreeNode,path:list):
            nonlocal ret
            if not node:
                return 
            path.append(chr(ord('a')+node.val))
            if not node.left and not node.right:
                ret=min(ret,''.join(reversed(path)))
            else:
                traverse(node.left,path)
                traverse(node.right,path)
            path.pop()
        traverse(root,[])
        return ret
            


# @lc code=end
root = '[2,0,1,null,null,0]'
assert Solution().smallestFromLeaf(TreeNode.build(root))=='abc'
root = '[4,0,1,1]'
assert Solution().smallestFromLeaf(TreeNode.build(root))=='bae'
root = '[3,9,20,null,null,15,7]'
assert Solution().smallestFromLeaf(TreeNode.build(root))=='hud'
root = '[2,2,1,null,1,0,null,0]'
assert Solution().smallestFromLeaf(TreeNode.build(root))=='abc'
root = [25,1,3,1,3,0,2]
assert Solution().smallestFromLeaf(TreeNode.build(root))=='adz'
root = [0,1,2,3,4,3,4]
assert Solution().smallestFromLeaf(TreeNode.build(root))=='dba'