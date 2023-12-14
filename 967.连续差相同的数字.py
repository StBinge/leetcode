#
# @lc app=leetcode.cn id=967 lang=python3
#
# [967] 连续差相同的数字
#
from sbw import *


# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        q = deque(list(range(1, 10)))
        for i in range(1, n):
            for j in range(len(q)):
                num = q.popleft()
                lowest = num % 10
                if k == 0:
                    q.append(num * 10 + lowest)
                    continue
                if lowest >= k:
                    q.append(num * 10 + lowest - k)
                if lowest + k < 10:
                    q.append(num * 10 + lowest + k)
        return list(q)


# @lc code=end
n = 2
k = 2
ret=[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(ret)

n = 2
k = 0
ret = [11, 22, 33, 44, 55, 66, 77, 88, 99]
assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(ret)

n = 3
k = 7
ret = [181, 292, 707, 818, 929]
assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(ret)

n = 2
k = 1
ret = [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
assert sorted(Solution().numsSameConsecDiff(n, k)) == sorted(ret)
