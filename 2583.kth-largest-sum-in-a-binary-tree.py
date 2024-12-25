#
# @lc app=leetcode.cn id=2583 lang=python3
# @lcpr version=30204
#
# [2583] 二叉树中的第 K 大层和
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level=[root]
        vals=[]
        while level:
            s=0
            nxt=[]
            for node in level:
                s+=node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if len(vals)==k:
                heapq.heappushpop(vals,s)
            else:
                heapq.heappush(vals,s)
            level=nxt
        return vals[0] if len(vals)==k else -1
# @lc code=end



#
# @lcpr case=start
# [5,8,9,2,1,3,7,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,3]\n1\n
# @lcpr case=end

#

