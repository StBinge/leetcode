#
# @lc app=leetcode.cn id=1524 lang=python3
#
# [1524] 和为奇数的子数组数目
#
from sbw import *
# @lc code=start
from math import comb
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odds=0
        evens=1
        total=0
        ret=0
        Mod=10**9+7
        for n in arr:
            total+=n
            ret+=odds if total%2==0 else evens
            if total%2:
                odds+=1
            else:
                evens+=1

        return ret % Mod

# @lc code=end
assert Solution().numOfSubarrays([1,2,3,4,5,6,7])==16
assert Solution().numOfSubarrays([7])==1
assert Solution().numOfSubarrays([100,100,99,99])==4
assert Solution().numOfSubarrays([2,4,6])==0
assert Solution().numOfSubarrays([1,3,5])==4
