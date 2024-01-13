#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏
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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        x_cnt=-1
        l_chid,r_child=-1,-1
        def dfs(node:TreeNode):
            nonlocal x_cnt,l_chid,r_child
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            tot=1+left+right
            if node.val==x:
                l_chid=left
                r_child=right
                x_cnt=tot
  
            return tot
        total=dfs(root)
        return total-x_cnt>x_cnt or l_chid>total-l_chid or r_child>total-r_child

    

# @lc code=end
root = [1,2,3]
n = 3
x = 1
assert Solution().btreeGameWinningMove(TreeNode.build(root),n,x)==False

root = [1,2,3,4,5,6,7,8,9,10,11]
n = 11
x = 3
assert Solution().btreeGameWinningMove(TreeNode.build(root),n,x)
