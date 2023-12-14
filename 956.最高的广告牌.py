#
# @lc app=leetcode.cn id=956 lang=python3
#
# [956] 最高的广告牌
#
from sbw import *
# @lc code=start
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp={0:0}
        for n in rods:
            for key,b in list(dp.items()):
                k,v=key+n,b+n
                dp[k]=max(dp.get(k,0),v)
                k,v=key-n,b
                dp[k]=max(dp.get(k,0),v)
        return dp[0]

# @lc code=end
assert Solution().tallestBillboard([1,2,3,6])==6
assert Solution().tallestBillboard([1,2,3,4,5,6])==10
assert Solution().tallestBillboard([1,2])==0
