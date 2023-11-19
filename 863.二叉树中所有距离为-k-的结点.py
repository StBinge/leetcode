#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        ret=[]

        def find(node:TreeNode,dis):
            if not node:
                return
            if dis==k:
                ret.append(node.val)
                return
            find(node.left,dis+1)
            find(node.right,dis+1)

        def reverse(node:TreeNode):

            if not node:
                return -1
            if node.val==target.val:
                find(node.right,1)
                find(node.left,1)
                return 1
            d=reverse(node.left)
            if d>0:
                if d==k:
                    ret.append(node.val)
                    return -1
                find(node.right,d+1)
                return d+1
            d=reverse(node.right)
            if d>0:
                if d==k:
                    ret.append(node.val)
                    return -1
                find(node.left,d+1)
                return d+1
            return -1
        reverse(root)
        return ret
# @lc code=end
root = TreeNode.build('[0,2,1,null,null,3]')
target = TreeNode(3)
k = 3
assert Solution().distanceK(root,target,k)==[2]

root = TreeNode.build('[0,1,null,3,2]')
target = TreeNode(2)
k = 1
assert Solution().distanceK(root,target,k)==[1]


root = TreeNode.build('[3,5,1,6,2,0,8,null,null,7,4]')
target = TreeNode(5)
k = 2
assert Solution().distanceK(root,target,k)==[7,4,1]
root = TreeNode.build('[1]')
target = TreeNode(1)
k = 3
assert Solution().distanceK(root,target,k)==[]