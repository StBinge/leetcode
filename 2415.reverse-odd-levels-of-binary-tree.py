#
# @lc app=leetcode.cn id=2415 lang=python3
# @lcpr version=30204
#
# [2415] 反转二叉树的奇数层
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [root]
        idx = 0
        while level and level[0].left:
            idx += 1
            nxt = []
            for node in level:
                nxt.append(node.left)
                nxt.append(node.right)
            if idx & 1:
                left, right = 0, len(nxt) - 1
                while left < right:
                    nxt[left].val, nxt[right].val = nxt[right].val, nxt[left].val
                    left += 1
                    right -= 1
            level = nxt
        return root


# @lc code=end
assert Solution().reverseOddLevels(
    TreeNode.build([2, 3, 5, 8, 13, 21, 34])
).to_str() == str([2, 5, 3, 8, 13, 21, 34])
#
# @lcpr case=start
# [2,3,5,8,13,21,34]\n
# @lcpr case=end

# @lcpr case=start
# [7,13,11]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]\n
# @lcpr case=end

#
