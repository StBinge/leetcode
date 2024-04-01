#
# @lc app=leetcode.cn id=1494 lang=python3
#
# [1494] 并行课程 II
#
from sbw import *
# @lc code=start
import itertools
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        if len(relations)==0:
            return (n-1)//k+1
        masks=[0]*n
        for first,second in relations:
            first-=1
            second-=1
            masks[second] |= 1<<first
        
        f=[30]*(1<<n)
        f[-1]=0
        for mask in range((1<<n)-2,-1,-1):
            can_mask=0
            for i in range(n):
                if mask & 1<<i ==0 and mask & masks[i]==masks[i]:
                    can_mask |= 1<<i
            if can_mask.bit_count()<=k:
                f[mask]=f[mask | can_mask]+1
                continue
            j=can_mask
            while j:
                j=(j-1) & can_mask
                if j.bit_count()==k:
                    f[mask]=min(f[mask],f[mask | j]+1)
        return f[0]

            

# @lc code=end

assert Solution().minNumberOfSemesters(3,[[1,3],[2,1]],3)==3
assert Solution().minNumberOfSemesters(n = 11, relations = [], k = 2)==6
assert Solution().minNumberOfSemesters(n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2)==4
assert Solution().minNumberOfSemesters(n = 4, relations = [[2,1],[3,1],[1,4]], k = 2)==3