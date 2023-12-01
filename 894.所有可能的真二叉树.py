#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的真二叉树
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
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # if n%2==0:
        #     return []
        memo={0:[],1:[TreeNode(0)]}
        def build(n):
            if n in memo:
                return memo[n]
            ans=[]
            for i in range(1,n,2):
                for l in build(i):
                    for r in build(n-1-i):
                        root=TreeNode(0)
                        root.left=l
                        root.right=r
                        ans.append(root)
            memo[n]=ans
            return ans
        build(n)
        return memo[n]

# @lc code=end
ret=Solution().allPossibleFBT(7)
for node in ret:
    node.print()

print()
ret=Solution().allPossibleFBT(3)
for node in ret:
    node.print()