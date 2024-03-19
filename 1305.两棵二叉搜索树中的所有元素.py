#
# @lc app=leetcode.cn id=1305 lang=python3
#
# [1305] 两棵二叉搜索树中的所有元素
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
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def yield_value(node:TreeNode):

            if node.left:
                yield from yield_value(node.left)
            yield node.val
            if node.right:
                yield from yield_value(node.right)
        
        if not root1 and not root2:
            return []
        if not root1 and root2:
            return list(yield_value(root2))
        if not root2 and root1:
            return list(yield_value(root1))
        itor1=yield_value(root1)
        itor2=yield_value(root2)
        ret=[]
        Max=10**6
        Min=-10**6
        n1=next(itor1)
        n2=next(itor2)
        while n1<Max or n2<Max:
            if n1<n2:
                ret.append(n1)
                n1=next(itor1,Max)
            else:
                ret.append(n2)
                n2=next(itor2,Max)
        return ret
# @lc code=end

assert Solution().getAllElements(None,None)==[]
assert Solution().getAllElements(None,TreeNode.build('[8,1]'))==[1,8]
assert Solution().getAllElements(TreeNode.build('[1,null,8]'),TreeNode.build('[8,1]'))==[1,1,8,8]
assert Solution().getAllElements(TreeNode.build([2,1,4]),TreeNode.build([1,0,3]))==[0,1,1,2,3,4]