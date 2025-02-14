#
# @lc app=leetcode.cn id=2327 lang=python3
# @lcpr version=30204
#
# [2327] 知道秘密的人数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        sums=[0]*(n+1)
        sums[1]=1
        mod = 10**9 + 7

        for i in range(2,n+1):
            f=sums[max(i-delay,0)]-sums[max(i-forget,0)]
            sums[i]=(sums[i-1]+f)%mod
                      
        return (sums[n]-sums[max(n-forget,0)])%mod


# @lc code=end
assert Solution().peopleAwareOfSecret(4, 1, 4) == 8
assert Solution().peopleAwareOfSecret(4, 1, 3) == 6
assert Solution().peopleAwareOfSecret(6, 2, 4) == 5


#
# @lcpr case=start
# 6\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n3\n
# @lcpr case=end

#
