#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
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
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # key=col index
        # value=[[rid,val],]
        # vals={0:[[0,root.val]]}
        vals={}
        # q=deque([[0,0,root]])
        q=[[0,0,root]]
        while q:
            r,c,node=q.pop()
            vals.setdefault(c,[]).append([r,node.val])
            if node.left:
                q.append([r+1,c-1,node.left])
            if node.right:
                q.append([r+1,c+1,node.right])
        

        ret=[]
        for k in sorted(vals.keys()):
            v=vals[k]
            v.sort()
            ret.append([x[1] for x in v])
        return ret

# @lc code=end
root = '[3,9,20,null,null,15,7]'
ret=[[9],[3,15],[20],[7]]
assert Solution().verticalTraversal(TreeNode.build(root))==ret

root = [1,2,3,4,6,5,7]
ret=[[4],[2],[1,5,6],[3],[7]]
assert Solution().verticalTraversal(TreeNode.build(root))==ret
