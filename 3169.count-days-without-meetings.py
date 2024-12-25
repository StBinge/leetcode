#
# @lc app=leetcode.cn id=3169 lang=python3
# @lcpr version=30204
#
# [3169] 无需开会的工作日
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: [x[0], -x[1]])
        meetings.append([days + 1, -1])
        ret = 0
        # pre_end=0
        cur_end = 0
        for s, e in meetings:
            if s <= cur_end:
                cur_end = max(cur_end, e)
            else:
                ret += s - cur_end - 1
                cur_end = e
        return ret


# @lc code=end

assert Solution().countDays(days=6, meetings=[[1, 6]]) == 0
assert Solution().countDays(days=5, meetings=[[2, 4], [1, 3]]) == 1
assert Solution().countDays(days=10, meetings=[[5, 7], [1, 3], [9, 10]]) == 2

#
# @lcpr case=start
# 10\n[[5,7],[1,3],[9,10]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[2,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# 6\n[[1,6]]\n
# @lcpr case=end

#
