#
# @lc app=leetcode.cn id=1997 lang=python3
# @lcpr version=30204
#
# [1997] 访问完所有房间的第一天
#

from sbw import *


def count(next_visit: list):
    N = len(next_visit)
    cnt = [0] * N
    f = [0] * N
    day = 0
    for i in range(N):
        idx = i
        while idx <= i:
            cnt[idx] ^= 1
            if cnt[idx] == 0:
                idx += 1
            else:
                idx = next_visit[idx]
            day += 1
        f[i] = day
    return f


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # ff = count(nextVisit)
        mod = 10**9 + 7
        N = len(nextVisit)
        f = [0] * (N + 1)
        # pre_sums=[0]
        # pre_sums.append(f[0])
        for i in range(1, N):
            f[i] = f[i - 1] *2 - f[nextVisit[i - 1]] + 2
            f[i] %= mod
        return f[N-1]


# @lc code=end
assert Solution().firstDayBeenInAllRooms([0, 0]) == 2
assert Solution().firstDayBeenInAllRooms([0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 1, 8]) == 2048
assert Solution().firstDayBeenInAllRooms(nextVisit=[0, 1, 2, 0]) == 6
assert Solution().firstDayBeenInAllRooms([0, 0, 2]) == 6
assert Solution().firstDayBeenInAllRooms([0, 0]) == 2


#
# @lcpr case=start
# [0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,0]\n
# @lcpr case=end

#
