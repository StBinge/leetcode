#
# @lc app=leetcode.cn id=1703 lang=python3
#
# [1703] 得到连续 K 个 1 的最少相邻交换次数
#
from sbw import *
# @lc code=start
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        g=[]
        presum=[0]
        for i,n in enumerate(nums):
            if n==0:
                continue
            g.append(i-len(g))
            presum.append(presum[-1]+g[-1])
        N=len(g)
        ret=float('inf')
        for i in range(N-k+1):
            mid=i+k//2
            r=g[mid]
            ret=min(ret,r*(1-k%2)+presum[i+k]-presum[mid+1]-presum[mid]+presum[i])
        return ret

# @lc code=end
assert Solution().minMoves(nums = [1,0,0,1,0,1], k = 2)==1
