#
# @lc app=leetcode.cn id=2523 lang=python3
# @lcpr version=30204
#
# [2523] 范围内最接近的两个质数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[1]=False
        for i in range(2, right + 1):
            if not is_prime[i]:
                continue
            for j in range(i + i, right + 1, i):
                is_prime[j] = False
        mi = float("inf")
        pre = -1
        ret = [-1, -1]
        for i in range(left, right + 1):
            if is_prime[i]:
                if pre > 0:
                    dif = i - pre
                    if dif < mi:
                        mi = dif
                        ret = [pre, i]
                        if mi==1:
                            return ret
                pre = i
        return ret


# @lc code=end
assert Solution().closestPrimes(1,1000000) == [2,3]
assert Solution().closestPrimes(left=10, right=19) == [11, 13]


#
# @lcpr case=start
# 10\n19\n
# @lcpr case=end

# @lcpr case=start
# 4\n6\n
# @lcpr case=end

#
