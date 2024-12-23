#
# @lc app=leetcode.cn id=面试题 04.02 lang=python3
# @lcpr version=30204
#
# [面试题 04.02] 最小高度树
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bulid(left,right):
            if left>right:
                return None
            mid=(left+right)>>1
            node=TreeNode(nums[mid])
            node.left=bulid(left,mid-1)
            node.right=bulid(mid+1,right)
            return node
        return bulid(0,len(nums)-1)
# @lc code=end

print(Solution().sortedArrayToBST([-10,-3,0,5,9]).to_str())

