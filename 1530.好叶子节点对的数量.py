#
# @lc app=leetcode.cn id=1530 lang=python3
#
# [1530] 好叶子节点对的数量
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
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def traverse(node: TreeNode):            
            dist=[0]*distance
            if not node:
                return (dist,-1)
            if not node.left and not node.right:
                dist[0]=1
                return (dist,0)
            left_dist,left_ret=traverse(node.left)
            right_dist,right_ret=traverse(node.right)
            ret=0
            if  right_ret>=0 and left_ret>=0:
                for i in range(distance-1):
                    for j in range(distance-2-i,-1,-1):
                        ret+=left_dist[i]*right_dist[j]
            for i in range(1,distance):
                dist[i]+=left_dist[i-1]+right_dist[i-1]
            return (dist,ret)
        ret= traverse(root)[1]
        return ret


# @lc code=end

assert Solution().countPairs(TreeNode.build("[78,15,81,73,98,36,null,30,null,63,32]"), 6) == 6
assert Solution().countPairs(TreeNode.build("[1,1,1]"), 2) == 1
assert Solution().countPairs(TreeNode.build("[100]"), 1) == 0
assert Solution().countPairs(TreeNode.build("[7,1,4,6,null,5,3,null,null,null,null,null,2]"), 3) == 1
assert Solution().countPairs(TreeNode.build("[1,2,3,4,5,6,7]"), 3) == 2
assert Solution().countPairs(TreeNode.build("[1,2,3,null,4]"), 3) == 1
