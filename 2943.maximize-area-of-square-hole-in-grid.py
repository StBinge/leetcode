#
# @lc app=leetcode.cn id=2943 lang=python3
# @lcpr version=30204
#
# [2943] 最大化网格图中正方形空洞的面积
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        vBars.sort()
        hBars.sort()
        return (min(
            max(Counter(i-x for i,x in enumerate(hBars)).values()),
            max(Counter(i-x for i,x in enumerate(vBars)).values()))+1)**2


# @lc code=end
assert Solution().maximizeSquareHoleArea(4, 40, [5, 3, 2, 4], [36, 41, 6, 34, 33]) == 9
assert Solution().maximizeSquareHoleArea(14, 4, [13], [3, 4, 5, 2]) == 4
assert Solution().maximizeSquareHoleArea(n=2, m=3, hBars=[2, 3], vBars=[2, 3, 4]) == 9
assert Solution().maximizeSquareHoleArea(n=1, m=1, hBars=[2], vBars=[2]) == 4
assert Solution().maximizeSquareHoleArea(n=2, m=1, hBars=[2, 3], vBars=[2]) == 4


#
# @lcpr case=start
# 2\n1\n[2,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n[2]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 2\n3\n[2,3]\n[2,3,4]\n
# @lcpr case=end

#
