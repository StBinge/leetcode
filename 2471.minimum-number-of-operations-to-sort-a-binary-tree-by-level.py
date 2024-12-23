#
# @lc app=leetcode.cn id=2471 lang=python3
# @lcpr version=30204
#
# [2471] 逐层排序二叉树所需的最少操作数目
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
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q=[root]
        while q:
            vals=[]
            nxt=[]
            for node in q:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
# @lc code=end



#
# @lcpr case=start
# [1,4,3,7,6,8,5,null,null,null,null,9,null,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,7,6,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

