#
# @lc app=leetcode.cn id=1925 lang=python3
# @lcpr version=30204
#
# [1925] 统计平方和三元组的数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        squres = [i * i for i in range(1, n + 1)]
        s = set(squres)
        N = len(squres)
        Max = n * n
        for i in range(N - 1):
            for j in range(i + 1, N):
                if squres[i] + squres[j] > Max:
                    break
                if squres[i] + squres[j] in s:
                    ret += 2
        return ret


# @lc code=end
assert Solution().countTriples(10) == 4
assert Solution().countTriples(5) == 2


#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
