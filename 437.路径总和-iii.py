#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        def dfs(root,cur):
            if not root:
                return 0
            
            cur+=root.val
            t=cur-targetSum
            ret=prefix[t]
            prefix[cur]+=1
            ret+=dfs(root.left,cur)
            ret+=dfs(root.right,cur)
            prefix[cur]-=1
            return ret
        return dfs(root,0)
# @lc code=end
root=TreeNode(1,right=TreeNode(2,right=TreeNode(3,right=TreeNode(4,right=TreeNode(5)))))

assert Solution().pathSum(root,3)==2