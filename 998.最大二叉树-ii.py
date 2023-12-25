#
# @lc app=leetcode.cn id=998 lang=python3
#
# [998] 最大二叉树 II
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
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent,cur=None,root
        while cur:
            if val>cur.val:
                if not parent:
                    return TreeNode(val,cur)
                else:
                    parent.right= TreeNode(val,cur)
                    return root
            else:
                parent=cur
                cur=cur.right
        parent.right=TreeNode(val)
        return root
# @lc code=end
root = '[5,2,3,null,1]'
val = 4
ret='[5,2,4,null,1,3]'
assert Solution().insertIntoMaxTree(TreeNode.build(root),val).to_str()==ret

root = '[5,2,4,null,1]'
val = 3
ret='[5,2,4,null,1,null,3]'
assert Solution().insertIntoMaxTree(TreeNode.build(root),val).to_str()==ret

root = '[4,1,3,null,null,2]'
val = 5
ret='[5,4,null,1,3,null,null,2]'
assert Solution().insertIntoMaxTree(TreeNode.build(root),val).to_str()==ret
