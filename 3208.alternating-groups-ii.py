#
# @lc app=leetcode.cn id=3208 lang=python3
# @lcpr version=30204
#
# [3208] 交替组 II
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        cnt = 1
        ret = 0
        for i in range(1, N + k - 1):
            if colors[i % N] == colors[(i - 1) % N]:
                cnt = 0
            cnt += 1
            ret += cnt >= k
        return ret


# @lc code=end
assert Solution().numberOfAlternatingGroups([0, 1, 0, 1], 3) == 4
assert Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 0, 1, 0, 1], k=6) == 2
assert Solution().numberOfAlternatingGroups(colors=[1, 1, 0, 1], k=4) == 0
assert Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 1, 0], k=3) == 3


#
# @lcpr case=start
# [0,1,0,1,0]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,0,1,0,1]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,1]\n4\n
# @lcpr case=end

#
