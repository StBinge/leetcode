#
# @lc app=leetcode.cn id=1969 lang=python3
# @lcpr version=30204
#
# [1969] 数组元素的最小非零乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        def quick_mul(base,exp):
            ret=1
            while exp:
                if exp & 1:
                    ret=ret*base%mod
                base=base*base %mod
                exp//=2
            return ret
                
        mod=10**9+7
        n=(1<<p)-1
        cnt=(1<<p-1) -1
        return n*quick_mul(n-1,cnt)%mod
# @lc code=end
assert Solution().minNonZeroProduct(22)==106294648
assert Solution().minNonZeroProduct(4)==581202553
assert Solution().minNonZeroProduct(3)==1512
assert Solution().minNonZeroProduct(2)==6
assert Solution().minNonZeroProduct(1)==1


#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

