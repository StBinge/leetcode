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
            return (n-1)//k +1
        
        need=[0]*(1<<n)
        for x,y in relations:
            x-=1
            y-=1
            need[1<<y] |= 1<<x
        
        f=[float('inf')]*(1<<n)
        f[0]=0
        for i in range(1,1<<n):
            need[i]=need[i&(i-1)] | need[i&(-i)]
            if i & need[i] !=i:
                continue
            sub=i ^ need[i]
            if sub.bit_count()<=k:
                f[i]=min(f[i],f[i ^ sub]+1)
                continue
            valid=sub
            while sub:
                sub=(sub-1) & valid
                if sub.bit_count()<=k:
                    f[i]=min(f[i],f[i ^ sub]+1)
                
        return f[-1]
            

# @lc code=end

assert Solution().minNumberOfSemesters(3,[[1,3],[2,1]],3)==3
assert Solution().minNumberOfSemesters(n = 11, relations = [], k = 2)==6
assert Solution().minNumberOfSemesters(n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2)==4
assert Solution().minNumberOfSemesters(n = 4, relations = [[2,1],[3,1],[1,4]], k = 2)==3