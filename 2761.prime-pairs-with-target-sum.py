#
# @lc app=leetcode.cn id=2761 lang=python3
# @lcpr version=30204
#
# [2761] 和等于目标值的质数对
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * n
        for i in range(2, n):
            if not is_prime[i]:
                continue
            for j in range(i + i, n, i):
                is_prime[j] = False
        if n%2:
            return [[2,n-2]] if is_prime[n-2] and n>3 else []
        ret = []
        for i in range(2, n // 2 + 1):
            if is_prime[i] and is_prime[n - i]:
                ret.append([i, n - i])
        return ret


# @lc code=end
assert Solution().findPrimePairs(2) == []
assert Solution().findPrimePairs(10) == [[3, 7], [5, 5]]


#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
