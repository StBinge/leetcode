#
# @lc app=leetcode.cn id=2787 lang=python3
# @lcpr version=30204
#
# [2787] 将一个数字表示成幂的和的方案数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
    
        mod=10**9+7
        f=[0]*(n+1)
        f[0]=1
        for i in range(1,n+1):
            v=i**x
            if v>n:
                break
            for j in range(n,v-1,-1):
                f[j]+=f[j-v]
        return f[n]%mod
# @lc code=end
assert Solution().numberOfWays(233,1)==328423915
assert Solution().numberOfWays(213,1)==55852583
assert Solution().numberOfWays(2,1)==1
assert Solution().numberOfWays(10,2)==1


#
# @lcpr case=start
# 10\n2\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

#

