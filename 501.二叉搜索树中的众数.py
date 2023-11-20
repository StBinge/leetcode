#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import *
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        base=10**6
        cnt=1
        max_cnt=0
        ret=[]
        def update(val:int):
            nonlocal base,cnt,max_cnt,ret
            if base==val:
                cnt+=1
            else:
                base=val
                cnt=1
            if cnt>max_cnt:
                max_cnt=cnt
                ret=[val]
            elif cnt==max_cnt:
                ret.append(val)
        
        cur=root
        while cur:
            if not cur.left:
                update(cur.val)
                cur=cur.right
                continue
            pre=cur.left
            while pre.right and pre.right!=cur:
                pre=pre.right
            if not pre.right:
                pre.right=cur
                cur=cur.left
            else:
                pre.right=None
                update(cur.val)
                cur=cur.right

        return ret
# @lc code=end

root=TreeNode(1,right=TreeNode(2))
r=Solution().findMode(root)
print(r)