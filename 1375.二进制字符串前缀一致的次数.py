#
# @lc app=leetcode.cn id=1375 lang=python3
#
# [1375] 二进制字符串前缀一致的次数
#
from sbw import *
# @lc code=start
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        L=len(flips)
        ma=-1
        ret=0
        for i in range(L):
            ma=max(flips[i]-1,ma)
            if ma==i:
                ret+=1
        return ret
# @lc code=end
assert Solution().numTimesAllBlue([4,1,2,3])==1
assert Solution().numTimesAllBlue([3,2,4,1,5])==2
