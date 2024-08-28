#
# @lc app=leetcode.cn id=2001 lang=python3
# @lcpr version=30204
#
# [2001] 可互换矩形的组数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for w, h in rectangles:
            # g = math.gcd(w, h)
            cnt[w/h] += 1
        return sum((v - 1) * v // 2 for v in cnt.values())


# @lc code=end
assert Solution().interchangeableRectangles([[4, 5], [7, 8]]) == 0
assert (
    Solution().interchangeableRectangles(
        rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]]
    )
    == 6
)


#
# @lcpr case=start
# [[4,8],[3,6],[10,20],[15,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,5],[7,8]]\n
# @lcpr case=end

#
