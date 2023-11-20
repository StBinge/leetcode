#
# @lc app=leetcode.cn id=851 lang=python3
#
# [851] 喧闹和富有
#
from typing import List
# @lc code=start
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
 

        edges={}
        for src,dst in richer:
            edges.setdefault(dst,[]).append(src)
        n=len(quiet)
        # riches=[set() for _ in range(n)]
        ret=[-1]*n

        def dfs(idx):
            if ret[idx]!=-1:
                return ret[idx]
            res=idx
            for nxt in edges.get(idx,[]):
                t=dfs(nxt)
                if quiet[t]<quiet[res]:
                    res=t
            return res

        
        for i in range(n):
            ret[i]=dfs(i)
            
        return ret

# @lc code=end
richer = []
quiet = [0]
ret=[0]
assert Solution().loudAndRich(richer,quiet)==ret

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
ret=[5,5,2,5,4,5,6,7]
assert Solution().loudAndRich(richer,quiet)==ret