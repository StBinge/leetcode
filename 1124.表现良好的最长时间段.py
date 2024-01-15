#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#
from sbw import *
# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        L=len(hours)

        pos=[0]*(L+2)
        s=0
        ret=0
        for i,h in enumerate(hours,1):
            s-=1 if h>8 else -1
            if s<0:
                ret=i
            else:
                if pos[s+1]:
                    ret=max(ret,i-pos[s+1])
                if pos[s]==0:
                    pos[s]=i
        return ret

# @lc code=end
assert Solution().longestWPI([9,9,6,0,6,6,9])==3
assert Solution().longestWPI([6,6,6])==0
