#
# @lc app=leetcode.cn id=1040 lang=python3
#
# [1040] 移动石子直到连续 II
#
from sbw import *
# @lc code=start
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        L=len(stones)
        G=stones[-1]-stones[0]+1-L
        if G==0:
            return [0,0]
        l_gap=stones[-2]-stones[0]-1-(L-3)
        r_gap=stones[-1]-stones[1]-1-(L-3)
        ma=max(l_gap,r_gap)

        if l_gap==0 or r_gap==0:
            return [min(2,ma),ma]
        l=max_cnt=0
        for r, s in enumerate(stones):
            while s-stones[l]+1>L:
                l+=1
            max_cnt=max(max_cnt,r-l+1)
        return [L-max_cnt,ma]

# @lc code=end
assert Solution().numMovesStonesII([8,7,6,5,1000000000])==[2,999999991]
assert Solution().numMovesStonesII([100,101,104,102,103])==[0,0]
assert Solution().numMovesStonesII([6,5,4,3,10])==[2,3]
assert Solution().numMovesStonesII([7,4,9])==[1,2]
