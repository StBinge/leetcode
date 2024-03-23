#
# @lc app=leetcode.cn id=1269 lang=python3
#
# [1269] 停在原地的方案数
#
from sbw import *
# @lc code=start
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        prev=defaultdict(int)
        prev[0]=1
        Mod=10**9+7
        for i in range(steps):
            step_left=steps-i
            cur=defaultdict(int)
            for k,v in prev.items():
                if k > step_left:
                    cur[k-1]+=v
                else:
                    cur[k]+=v
                    if k+1<arrLen:
                        cur[k+1]+=v
                    if k>0:
                        cur[k-1]+=v
            for k in cur:
                cur[k]%=Mod
            prev=cur
        return prev[0]
# @lc code=end
assert Solution().numWays(27,7)==127784505
assert Solution().numWays(4,2)==8
assert Solution().numWays(2,4)==2
assert Solution().numWays(3,2)==4
