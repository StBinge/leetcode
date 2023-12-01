#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        ret=0
        
        pre=-2
        for i in range(L:=len(flowerbed)):
            if flowerbed[i]:
                ret+=(i-pre-2)//2
                if ret>=n:
                    return True
                pre=i
        ret+=(len(flowerbed)-pre-1)//2
        return ret>=n
# @lc code=end

assert Solution().canPlaceFlowers([1,0,0,0,1,0,0],2)==True
assert Solution().canPlaceFlowers([1,0,0,0,1],0)==True
assert Solution().canPlaceFlowers([1,0,0,0,1],1)==True
assert Solution().canPlaceFlowers([1,0,0,0,1],2)==False