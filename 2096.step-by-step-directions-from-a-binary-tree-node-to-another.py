#
# @lc app=leetcode.cn id=2096 lang=python3
# @lcpr version=30204
#
# [2096] 从二叉树一个节点到另一个节点每一步的方向
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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent={}
        def dfs(node:TreeNode):
            if node.left:
                parent[node.left.val]=node
                dfs(node.left)
            if node.right:
                parent[node.right.val]=node
                dfs(node.right)
        
        dfs(root)

        def path(val):
            ret=[]
            while val in parent:
                p=parent[val]
                if p.left and val==p.left.val:
                    ret.append('L')
                else:
                    ret.append('R')
                val=p.val
            return ret[::-1]
        
        spath=path(startValue)
        tpath=path(destValue)

        l=min(len(spath),len(tpath))
        for i in range(min(len(spath),len(tpath))):
            if spath[i]!=tpath[i]:
                l=i
                break
        ret= 'U'*(len(spath)-l)+''.join(tpath[l:])
        return ret
            
# @lc code=end
assert Solution().getDirections(TreeNode.build('[13,5,4,7,null,8,6,3,null,null,12,9,1,null,null,11,null,null,10,null,null,null,null,2]'),3,2)=='UUURRLRL'
assert Solution().getDirections(TreeNode.build('[1,3,8,7,null,4,5,6,null,null,null,null,null,null,2]'),2,1)=='UUUU'
assert Solution().getDirections(TreeNode.build([2,1]),2,1)=='L'
assert Solution().getDirections(TreeNode.build([3,1,2]),2,1)=='UL'


#
# @lcpr case=start
# [5,1,2,3,null,6,4]\n3\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n1\n
# @lcpr case=end

#

