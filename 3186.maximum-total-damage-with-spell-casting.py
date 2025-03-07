#
# @lc app=leetcode.cn id=3186 lang=python3
# @lcpr version=30204
#
# [3186] 施咒的最大总伤害
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt=Counter(power)
        sorted_nums=sorted(cnt.keys())
        N=len(sorted_nums)
        f=[0]*(N+1)
        j=0
        for i,x in enumerate(sorted_nums):
            while sorted_nums[j]+2<x:
                j+=1
            f[i+1]=max(f[i],f[j]+x*cnt[x])
        return f[-1]
# @lc code=end
assert Solution().maximumTotalDamage( [7,1,6,6])==13
assert Solution().maximumTotalDamage([1,1,3,4])==6


#
# @lcpr case=start
# [1,1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,6,6]\n
# @lcpr case=end

#

