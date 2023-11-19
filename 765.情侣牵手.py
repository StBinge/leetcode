#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#
from typing import List
# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        L=len(row)
        N=L//2
        p=list(range(N))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        def union(x,y):
            p[find(x)]=p[find(y)]
        
        for i in range(0,L,2):
            union(row[i]//2,row[i+1]//2)
        
        cnt=0
        for i in range(N):
            if p[i]==i:
                cnt+=1
        return N-cnt

# @lc code=end
row = [0,2,1,3]
assert Solution().minSwapsCouples(row)==1
row = [3,2,0,1]
assert Solution().minSwapsCouples(row)==0
