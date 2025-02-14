#
# @lc app=leetcode.cn id=2266 lang=python3
# @lcpr version=30204
#
# [2266] 统计打字方案数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod=10**9+7
        f=[1,1,2,4]
        g=[1,1,2,4]
        for i in range(10**5-3):
            f.append((f[-1]+f[-2]+f[-3])%mod)
            g.append((g[-1]+g[-2]+g[-3]+g[-4])%mod)
        ans=1
        for x,y in groupby(pressedKeys):
            cnt=len(list(y))
            ans=ans*(g[cnt] if x in '79' else f[cnt])%mod
        return ans
# @lc code=end+
assert Solution().countTexts('222222222222222222222222222222222222')==82876089
assert Solution().countTexts('22233')==8


#
# @lcpr case=start
# "22233"\n
# @lcpr case=end

# @lcpr case=start
# "222222222222222222222222222222222222"\n
# @lcpr case=end

#

