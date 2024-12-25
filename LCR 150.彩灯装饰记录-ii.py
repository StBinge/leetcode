#
# @lc app=leetcode.cn id=LCR 150 lang=python3
# @lcpr version=30204
#
# [LCR 150] 彩灯装饰记录 II
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
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret=[]
        if not root:
            return ret
        q=[root]
        while q:
            nxt=[]
            ret.append([])
            for node in q:
                ret[-1].append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            q=nxt
        return ret
# @lc code=end



#
# @lcpr case=start
# [8,17,21,18,null,null,6]\n
# @lcpr case=end

#

