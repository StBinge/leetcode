#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#
from sbw import *
# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f=[0,float('-inf'),float('-inf')]
        for n in nums:
            g=[0]*3
            for i in range(3):
                g[(i+n)%3]=max(f[(i+n)%3],f[i]+n)
            f=g
        return f[0]
# @lc code=end
assert Solution().maxSumDivThree(nums = [3,6,5,1,8])==18
assert Solution().maxSumDivThree(nums = [1,2,3,4,4])==12
assert Solution().maxSumDivThree(nums = [4])==0
