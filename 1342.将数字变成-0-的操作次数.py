#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#
from sbw import *
# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num==0:
            return 0
        bits=0
        ones=0
        while num>0:
            bits+=1
            ones+=num&1
            num>>=1
        return bits+ones-1
# @lc code=end
assert Solution().numberOfSteps(0)==0
assert Solution().numberOfSteps(8)==4
assert Solution().numberOfSteps(14)==6
