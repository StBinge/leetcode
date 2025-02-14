#
# @lc app=leetcode.cn id=3001 lang=python3
# @lcpr version=30204
#
# [3001] 捕获黑皇后需要的最少移动次数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        # one move
        if a == e != c:
            return 1
        if a == c == e and (d < min(b, f) or d > max(b, f)):
            return 1

        if b == f != d:
            return 1
        if b == d == f and (c < min(a, e) or c > max(a, e)):
            return 1

        if abs(c - e) == abs(d - f):
            if (f - b) * (a - c) != (b - d) * (e - a):
                return 1
            if a<min(c,e) or a>max(c,e):
                return 1
            return 2

        return 2


# @lc code=end
assert Solution().minMovesToCaptureTheQueen(6, 8, 6, 6, 6, 3) == 2
assert Solution().minMovesToCaptureTheQueen(4, 3, 3, 4, 2, 5) == 1
assert Solution().minMovesToCaptureTheQueen(4, 3, 3, 4, 2, 5) == 1
assert Solution().minMovesToCaptureTheQueen(4, 5, 7, 8, 2, 3) == 2


#
# @lcpr case=start
# 1\n1\n8\n8\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n3\n3\n4\n5\n2\n
# @lcpr case=end

#
