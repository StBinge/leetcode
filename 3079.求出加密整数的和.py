#
# @lc app=leetcode.cn id=3079 lang=python3
#
# [3079] 求出加密整数的和
#
from sbw import *
# @lc code=start
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ret=0
        for n in nums:
            ma=0
            base=0
            while n:
                n,m=divmod(n,10)
                ma=max(ma,m)
                base=base*10+1
            ret+=ma*base
        return ret
# @lc code=end
assert Solution().sumOfEncryptedInt(nums = [10,21,31])==66
assert Solution().sumOfEncryptedInt(nums = [1,2,3])==6
