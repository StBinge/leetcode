#
# @lc app=leetcode.cn id=1395 lang=python3
#
# [1395] 统计作战单位数
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        L=len(rating)
        pos_map={n:(i+1) for i,n in enumerate(sorted(rating))}
        tree=[0]*(L+1)
        small=[0]*L
        large=[0]*L
        def low_bit(x):
            return x&(-x)
        def add(x):
            while x<=L:
                tree[x]+=1
                x+=low_bit(x)
        def get(x):
            ret=0
            while x:
                ret+=tree[x]
                x-=low_bit(x)
            return ret
        for i,r in enumerate(rating):
            idx=pos_map[r]
            small[i]=get(idx-1)
            add(pos_map.get(r))
        
        tree=[0]*(L+1)
        for i in range(L-1,-1,-1):
            idx=pos_map[rating[i]]
            large[i]=get(L)-get(idx)
            add(idx)
        
        ret=0
        for i in range(L):
            ret+=small[i]*large[i]+(i-small[i])*(L-1-i-large[i])
        return ret
# @lc code=end
assert Solution().numTeams([1,2,3,4])==4
assert Solution().numTeams([2,1,3])==0
assert Solution().numTeams([2,5,3,4,1])==3
