#
# @lc app=leetcode.cn id=1722 lang=python3
#
# [1722] 执行交换操作后的最小汉明距离
#
from sbw import *
# @lc code=start
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        if not allowedSwaps:
            return sum(x!=y for x,y in zip(source,target))
        N=len(source)
        p=list(range(N))
        size=[1]*N
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]

        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return px
            if size[px]<size[py]:
                px,py=py,px
            p[py]=px
            return px
        
        for x,y in allowedSwaps:
            union(x,y)
        
        counter={}
        for i,v in enumerate(source):
            cnt=counter.setdefault(find(i),defaultdict(int))
            cnt[v]+=1
        
        ret=0
        for i,v in enumerate(target):
            cnt=counter[find(i)]
            if cnt.get(v,0)>0:
                cnt[v]-=1
            else:
                ret+=1
        return ret
# @lc code=end
assert Solution().minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]])==0
assert Solution().minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = [])==2
assert Solution().minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]])==1
