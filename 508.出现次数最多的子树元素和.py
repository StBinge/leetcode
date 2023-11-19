#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional,List
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counter={}
        max_cnt=0
        ret=[]
        def calc(root:TreeNode):
            nonlocal max_cnt,ret,counter
            if not root:
                return 0
            s=root.val+calc(root.left)+calc(root.right)
            cnt=counter.get(s,0)+1
            counter[s]=cnt
            if cnt>max_cnt:
                ret=[s]
                max_cnt=cnt
            elif cnt==max_cnt:
                ret.append(s)
            return s
        calc(root)
        return ret
# @lc code=end
root=TreeNode(5,left=TreeNode(2),right=TreeNode(-3))
r= Solution().findFrequentTreeSum(root)
print(r)

root=TreeNode(5,left=TreeNode(2),right=TreeNode(-5))
r= Solution().findFrequentTreeSum(root)
print(r)
