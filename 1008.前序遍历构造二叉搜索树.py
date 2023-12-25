#
# @lc app=leetcode.cn id=1008 lang=python3
#
# [1008] 前序遍历构造二叉搜索树
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
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        L=len(preorder)
        root=TreeNode(preorder[0])
        stack=[root]
        for i in range(1,L):
            cur_node=TreeNode(preorder[i])
            pnode=stack[-1]
            while stack and stack[-1].val<cur_node.val:
                pnode=stack.pop()
            
            if pnode.val<cur_node.val:
                pnode.right=cur_node
            else:
                pnode.left=cur_node
            stack.append(cur_node)
        return root
# @lc code=end
preorder = [1,3]
ret= '[1,null,3]'
assert Solution().bstFromPreorder(preorder).to_str()==ret

preorder = [8,5,1,7,10,12]
ret='[8,5,10,1,7,null,12]'
assert Solution().bstFromPreorder(preorder).to_str()==ret