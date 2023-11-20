#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def travers(root:TreeNode):
            if not root:
                return [0,0] #inclue self, not incule self
            
            left=travers(root.left)
            right=travers(root.right)
            not_inlcue=max(left)+max(right)
            include=root.val+left[1]+right[1]
            return [include,not_inlcue]

        res= travers(root)
        return max(res)

# @lc code=end
root=TreeNode.build([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])
assert Solution().rob(root)==690

root=TreeNode.build([3,2,3,None,3,None,1])
assert Solution().rob(root)==7

root=TreeNode.build([3,4,5,1,3,None,1])
assert Solution().rob(root)==9
