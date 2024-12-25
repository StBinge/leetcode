#
# @lc app=leetcode.cn id=LCR 052 lang=python3
# @lcpr version=30204
#
# [LCR 052] 递增顺序搜索树
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes=[root]
        dummy=TreeNode()
        cur=dummy
        while nodes:
            if nodes[-1].left:
                nodes.append(nodes[-1].left)
                nodes[-2].left=None
            else:
                cur.right=nodes.pop()
                cur=cur.right
                if cur.right:
                    nodes.append(cur.right)
        return dummy.right
# @lc code=end
    


#
# @lcpr case=start
# [5,3,6,2,4,null,8,1,null,null,null,7,9]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,7]\n
# @lcpr case=end

#

