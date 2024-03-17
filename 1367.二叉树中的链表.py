#
# @lc app=leetcode.cn id=1367 lang=python3
#
# [1367] 二叉树中的链表
#
from sbw import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        cur=head
        L=0
        h=0
        Mod=10**7+9
        while cur:
            L+=1
            h=((h*101)+cur.val)%Mod
            cur=cur.next
        High=(101**L)%Mod
        def traverse(node:TreeNode,path:list,s:int):
            if not node:
                return False
            path.append(node.val)
            s=((s*101)+node.val)%Mod
            if len(path)>L:
                s=(s-(path[-L-1]*High)%Mod)%Mod
            if s==h:
                return True
            ret= traverse(node.left,path,s) or traverse(node.right,path,s)
            path.pop()
            return ret
        return traverse(root,[],0)
# @lc code=end
assert Solution().isSubPath(ListNode.build([4,2,8]),TreeNode.build('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'))
assert Solution().isSubPath(ListNode.build([1,10]),TreeNode.build('[1,null,1,10,1,9]'))
assert Solution().isSubPath(ListNode.build([1,4,2,6,8]),TreeNode.build('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'))==False
assert Solution().isSubPath(ListNode.build([1,4,2,6]),TreeNode.build('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'))
