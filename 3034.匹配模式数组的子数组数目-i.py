#
# @lc app=leetcode.cn id=3034 lang=python3
#
# [3034] 匹配模式数组的子数组数目 I
#
from sbw import *
# @lc code=start
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        M=len(pattern)
        next=[0]*M
        j=0
        for i in range(1,M):
            while j>0 and pattern[i]!=pattern[j]:
                j=next[j-1]
            if pattern[j]==pattern[i]:
                j+=1
                next[i]=j
        
        j=0
        ret=0
        for x,y in pairwise(nums):
            code=(y>x)-(y<x)
            while j>0 and code!=pattern[j]:
                j=next[j-1]
            if code==pattern[j]:
                j+=1
                if j==M:
                    ret+=1
                    j=next[j-1]
        return ret
        
# @lc code=end
assert Solution().countMatchingSubarrays(nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1])==2
assert Solution().countMatchingSubarrays(nums = [1,2,3,4,5,6], pattern = [1,1])==4
