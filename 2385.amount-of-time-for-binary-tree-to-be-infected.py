#
# @lc app=leetcode.cn id=2385 lang=python3
# @lcpr version=30204
#
# [2385] 感染二叉树需要的总时间
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        ret=0
        def dfs(node:TreeNode):
            if not node:
                return 0
            nonlocal ret
            left_len=dfs(node.left)
            right_len=dfs(node.right)
            if node.val==start:
                ret=max(-left_len,-right_len)
                return 1
            if left_len>0 or right_len>0:
                ret=max(ret,abs(left_len)+abs(right_len))
                return max(left_len,right_len)+1
            return min(left_len,right_len)-1
        dfs(root)
        return ret


# @lc code=end
assert Solution().amountOfTime(TreeNode.build('[19,4,6,9,11,18,1,null,null,null,17,null,8,null,null,null,null,null,20]'),1)==5
assert Solution().amountOfTime(TreeNode.build('[1,5,3,null,4,10,6,9,2]'),3)==4
assert Solution().amountOfTime(TreeNode.build('[1]'),1)==0
assert Solution().amountOfTime(TreeNode.build('[5,2,3,4,null,null,null,1]'),4)==3


#
# @lcpr case=start
# [1,5,3,null,4,10,6,9,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

