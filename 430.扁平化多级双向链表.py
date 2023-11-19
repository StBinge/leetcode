#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
from typing import Optional
# @lc code=start
"""
# Definition for a Node.
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def dfs(node:Node)->Node:
            last=None
            cur=node
            while cur:
                if cur.child:
                    nxt=cur.next
                    child_last=dfs(cur.child)
                    cur.next=cur.child
                    cur.child.prev=cur
                    cur.child=None
                    child_last.next=nxt
                    if nxt:
                        nxt.prev=child_last
                    last=child_last
                    cur=nxt
                else:
                    last=cur
                    cur=cur.next
            return last
            

        dfs(head)
        return head

# @lc code=end

