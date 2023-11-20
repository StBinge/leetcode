#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        l=len(nums)
        presum=[0]*(l+1)
        for i,n in enumerate(nums):
            presum[i+1]=presum[i]+n
        q=deque()
        ret=l+1
        for i,s in enumerate(presum):
            while q and s-presum[q[0]]>=k:
                ret=min(ret,i-q.popleft())
            while q and s<=presum[q[-1]]:
                q.pop()
            q.append(i)
        return ret if ret!=l+1 else -1
# @lc code=end
assert Solution().shortestSubarray([18393,13015,39877,-46990,84110,-16361,-42889,-10085,46644,91545,71230,48090,34489,2788,56496,-32528,77455,-44282,80504,77949,70,74450,-4005,82184,-19401,49038,-10000,31028,26603,62302,76071,73298,-20008,-12421,-11904,-8055,50871,20857,56174,88271,37380,56974,85085,-29377,-39430,86935,-42349,-12415,-21752,95087],917790)==24
assert Solution().shortestSubarray([-23,51,-14,-6,36,33,76,-26,-6,58,-16,1,98,2,-20,48,-19,-41,-34,62],221)==9
assert Solution().shortestSubarray([84,-37,32,40,95],167)==3
assert Solution().shortestSubarray([-28,81,-20,28,-29],89)==3
assert Solution().shortestSubarray([27,20,79,87,-36,78,76,72,50,-26],453)==9
assert Solution().shortestSubarray([77,19,35,10,-14],19)==1
assert Solution().shortestSubarray([2,-1,2],3)==3
assert Solution().shortestSubarray([1,2],4)==-1
assert Solution().shortestSubarray([1],1)==1
