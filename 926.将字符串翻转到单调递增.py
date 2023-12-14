#
# @lc app=leetcode.cn id=926 lang=python3
#
# [926] 将字符串翻转到单调递增
#
from sbw import *
# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # l=len(s)
        d0=d1=0
        for c in s:
            d0,d1=d0,min(d0,d1)
            if c=='1':
                d0+=1
            else:
                d1+=1
        return min(d0,d1)
            

# @lc code=end
assert Solution().minFlipsMonoIncr("1001011110111101110000101101001010001010000101110111011000000110101111010110010011011011011010000010")==48
assert Solution().minFlipsMonoIncr("00011000")==2
assert Solution().minFlipsMonoIncr("010110")==2
assert Solution().minFlipsMonoIncr("00110")==1
