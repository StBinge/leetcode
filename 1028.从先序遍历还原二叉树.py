#
# @lc app=leetcode.cn id=1028 lang=python3
#
# [1028] 从先序遍历还原二叉树
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
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        val=0
        idx=0
        L =len(traversal)
        while idx<L and traversal[idx]!='-':
            val=val*10+int(traversal[idx])
            idx+=1
        
        root=TreeNode(val)
        stack=[[0,root]]
        d=0
        val=0
        for c in traversal[idx:]+'-':
            if c=='-':
                if val>0:
                    node=TreeNode(val)
                    val=0
                    while stack[-1][0]!=d-1:
                        stack.pop()
                    p=stack[-1][1]
                    if not p.left:
                        p.left=node
                    else:
                        p.right=node
                    stack.append([d,node])
                    d=0
                d+=1
            else:
                val=val*10+int(c)
        return root
# @lc code=end
assert Solution().recoverFromPreorder("3").to_str()=='[3]'

assert Solution().recoverFromPreorder("10-7--8").to_str()=='[10,7,null,8]'

assert Solution().recoverFromPreorder("1-401--349---90--88").to_str()=='[1,401,null,349,88,90]'

assert Solution().recoverFromPreorder("1-2--3--4-5--6--7").to_str()=='[1,2,5,3,4,6,7]'

assert Solution().recoverFromPreorder("1-2--3---4-5--6---7").to_str()=='[1,2,5,3,null,6,null,4,null,7]'
