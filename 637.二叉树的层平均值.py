#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

from sbw import *
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        cur_level=[root]
        ret=[]
        while cur_level:
            next_level=[]
            s=0
            for node in cur_level:
                s+=node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            ret.append(s/len(cur_level))
            cur_level=next_level
        return ret
# @lc code=end

