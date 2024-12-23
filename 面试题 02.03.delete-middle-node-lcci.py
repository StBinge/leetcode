#
# @lc app=leetcode.cn id=面试题 02.03 lang=python3
# @lcpr version=30204
#
# [面试题 02.03] 删除中间节点
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
# @lc code=end



#
# @lcpr case=start
# 节点 5 （位于单向链表 4->5->1->9 中）\n
# @lcpr case=end

#

