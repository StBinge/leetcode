#
# @lc app=leetcode.cn id=2521 lang=python3
# @lcpr version=30204
#
# [2521] 数组乘积中的不同质因数数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # is_prime=[True]*1001
        # for i in range(2,1001):
        #     if is_prime[i]:
        #         for j in range(2*i,1001,i):
        #             is_prime[j]=False

        vis = set()
        for n in nums:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    vis.add(i)
                    n //= i
                    while n%i==0:
                        n//=i
                i += 1
            if n > 1:
                vis.add(n)
        return len(vis)


# @lc code=end
assert Solution().distinctPrimeFactors([2, 4, 8, 16]) == 1
assert Solution().distinctPrimeFactors([2, 4, 3, 7, 10, 6]) == 4


#
# @lcpr case=start
# [2,4,3,7,10,6]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,8,16]\n
# @lcpr case=end

#
