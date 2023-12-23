#
# @lc app=leetcode.cn id=971 lang=python3
#
# [971] 翻转二叉树以匹配先序遍历
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
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        L=len(voyage)
        idx=0
        ret=[]
        def tranverse(node:TreeNode):
            nonlocal L,idx
            if idx==L or not node:
                return True
            if node and node.val!=voyage[idx]:
                return False

            idx+=1
            # _idx=idx
            if tranverse(node.left):
                return tranverse(node.right)
            # else:
            #     idx=_idx
            ret.append(node.val)
            return tranverse(node.right) and tranverse(node.left)
        if tranverse(root):
            return ret
        else:
            return [-1]
# @lc code=end
root = [1,2,3]
voyage = [1,2,3]
ret=[]
root=TreeNode.build(root)
assert sorted(Solution().flipMatchVoyage(root,voyage))==sorted(ret)

root = [1,2,3]
voyage = [1,3,2]
ret=[1]
root=TreeNode.build(root)
assert sorted(Solution().flipMatchVoyage(root,voyage))==sorted(ret)

root = [1,2]
voyage = [2,1]
ret=[-1]
root=TreeNode.build(root)
assert sorted(Solution().flipMatchVoyage(root,voyage))==sorted(ret)
