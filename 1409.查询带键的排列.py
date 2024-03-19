#
# @lc app=leetcode.cn id=1409 lang=python3
#
# [1409] 查询带键的排列
#
from sbw import *
# @lc code=start
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        L=len(queries)
        N=L+m
        bits=[0]*(N+1)
        def low_bit(x):
            return x&(-x)
        def add(x,val):
            while x<=N:
                bits[x]+=val
                x+=low_bit(x)
        def query(x):
            ret=0
            while x:
                ret+=bits[x]
                x-=low_bit(x)
            return ret
        
        pos=[0]*(m+1)
        for i in range(1,m+1):
            pos[i]=i+L
            add(i+L,1)
        ret=[]
        for i,q in enumerate(queries):
            cur=pos[q]
            add(cur,-1)
            ret.append(query(cur))
            pos[q]=cur=L-i
            add(cur,1)
        return ret

# @lc code=end
assert Solution().processQueries(queries = [3,1,2,1], m = 5)==[2,1,2,1]
