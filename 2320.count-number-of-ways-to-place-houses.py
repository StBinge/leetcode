#
# @lc app=leetcode.cn id=2320 lang=python3
# @lcpr version=30204
#
# [2320] 统计放置房子的方式数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        f0=f1=1
        mod=10**9+7
        for i in range(2,n+1):
            f0,f1=(f0+f1)%mod,f0
        return pow(f0+f1,2,mod)
# @lc code=end
assert Solution().countHousePlacements(2)==9
assert Solution().countHousePlacements(1)==4


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

