#
# @lc app=leetcode.cn id=1851 lang=python3
#
# [1851] 包含每个查询的最小区间
#
from sbw import *
# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        N=len(queries)
        intervals.sort(key=lambda x:x[1]-x[0])
        Q=sorted([[q,i] for i,q in enumerate(queries)])
        ret=[-1]*N
        p=list(range(N+1))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        
        for l,r in intervals:
            pos=bisect_left(Q,[l,-1])
            idx=find(pos)
            Len=r-l+1
            while idx<N and Q[idx][0]<=r:
                ret[Q[idx][1]]=Len
                p[idx]=idx+1
                idx=find(idx+1)
        return ret

            
# @lc code=end
assert Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22])==[2,-1,4,6]
assert Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])==[3,3,1,4]
