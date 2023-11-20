#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
from typing import List
# @lc code=start
class TreeNode:
    def __init__(self) -> None:
        self.left=None
        self.right=None
    
    def add(self,num:int):
        cur=self
        for k in range(30,-1,-1):
            bit=(num>>k) & 1
            if bit==0:
                if not cur.left:
                    cur.left=TreeNode()
                cur=cur.left
            else:
                if not cur.right:
                    cur.right=TreeNode()
                cur=cur.right
    
    def query(self,num:int):
        cur=self
        x=0
        for k in range(30,-1,-1):
            x<<=1
            bit=(num>>k) &1
            if bit==0:
                if cur.right:
                    cur=cur.right
                    x+=1
                else:
                    cur=cur.left
            else:
                if cur.left:
                    cur=cur.left
                    x+=1
                else:
                    cur=cur.right
            
        return x


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root=TreeNode()
        ret=0
        for i in range(1,len(nums)):
            root.add(nums[i-1])
            ret=max(ret,root.query(nums[i]))
        return ret
    
# @lc code=end
assert Solution().findMaximumXOR([3,10,5,25,2,8])==28
assert Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70])==127
