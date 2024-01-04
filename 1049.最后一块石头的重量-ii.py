#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S=sum(stones)
        L=len(stones)
        target=S//2
        f=[False]*(target+1)
        f[0]=True
        for i in range(L):
            for j in range(target,stones[i]-1,-1):
                if j>=stones[i]:
                    f[j]|=f[j-stones[i]]
                
        for t in range(target,-1,-1):
            if f[t]==True:
                return S-2*t
# @lc code=end
stones = [31,26,33,21,40]
assert Solution().lastStoneWeightII(stones)==5

stones=[2,7,4,1,8,1]
assert Solution().lastStoneWeightII(stones)==1
