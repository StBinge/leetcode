#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        l_num = 0
        check_val = 0
        compare_odd = lambda x, y: x > y
        compare_even = lambda x, y: x < y
        while level:
            nxt = []
            if l_num & 1:  # odd
                check_val = 0
                compare = compare_odd
            else:
                check_val = 1
                compare = compare_even
            pre=0 if l_num&1==0 else float('inf')

            for node in level:
                if node.val &1 !=check_val or not compare(pre,node.val):
                    return False
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
                pre=node.val
            level = nxt
            l_num += 1
        return True


# @lc code=end

assert Solution().isEvenOddTree(TreeNode.build("[11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]"))
assert Solution().isEvenOddTree(TreeNode.build("[1]"))
assert Solution().isEvenOddTree(TreeNode.build("[5,9,1,3,5,7]")) == False
assert Solution().isEvenOddTree(TreeNode.build("[5,4,2,3,3,7]")) == False
assert Solution().isEvenOddTree(
    TreeNode.build("[1,10,4,3,null,7,9,12,8,6,null,null,2]")
)
