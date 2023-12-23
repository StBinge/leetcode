#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#
from sbw import *
# @lc code=start
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        ret=0
        counter=Counter(x&y for x in nums for y in nums)
        for k in nums:
            sub=k=k^0xffff
            while True:
                ret+=counter.get(sub,0)
                if sub==0:
                    break
                sub=(sub-1)&k
        return ret
# @lc code=end
nums = [0,0,0]
assert Solution().countTriplets(nums)==27
nums = [2,1,3]
assert Solution().countTriplets(nums)==12
