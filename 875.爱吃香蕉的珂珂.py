#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        if h==n:
            return max(piles)
        # if sum(piles)<=h:
        #     return 1
        piles.sort()
        left=1
        right=piles[-1]
        ret=10**9
        while left<right:
            mid=(left+right)//2
            cnt=bisect.bisect_right(piles,mid)
            for i in range(cnt,n):
                cnt+=(piles[i]-1)//mid+1
            if cnt<=h:
                ret=mid
                right=mid
            else:
                left=mid+1
        return ret
# @lc code=end
piles=[312884470]
h=968709470
assert Solution().minEatingSpeed(piles,h)==1

piles=[312884470]
h=312884469
assert Solution().minEatingSpeed(piles,h)==2
piles=[30,11,23,4,20]
h=6
assert Solution().minEatingSpeed(piles,h)==23

piles = [30,11,23,4,20]
h = 5
assert Solution().minEatingSpeed(piles,h)==30

piles = [3,6,7,11]
h = 8
assert Solution().minEatingSpeed(piles,h)==4
