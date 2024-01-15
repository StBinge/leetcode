#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#
from sbw import *


# @lc code=start
class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        N = len(customers)
        if N <= minutes:
            return sum(customers)
        total = sum(customers[i] for i in range(N) if grumpy[i] == 0)
        r = 0
        cnt = sum(customers[i] * grumpy[i] for i in range(minutes))

        ret = cnt
        r = minutes
        for r in range(minutes, N):
            cnt += (
                customers[r] * grumpy[r] - customers[r - minutes] * grumpy[r - minutes]
            )
            ret = max(ret, cnt)

        return ret + total


# @lc code=end
args = exec_expression(
    "customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3"
)
assert Solution().maxSatisfied(**args) == 16
customers = [2, 4, 1, 4, 1]
grumpy = [1, 0, 1, 0, 1]
minutes = 2
assert Solution().maxSatisfied(customers, grumpy, minutes) == 10

customers = [4, 10, 10]
grumpy = [1, 1, 0]
minutes = 2
assert Solution().maxSatisfied(customers, grumpy, minutes) == 24

assert Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1) == 1

args = exec_expression(
    "customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3"
)
assert Solution().maxSatisfied(**args) == 16
