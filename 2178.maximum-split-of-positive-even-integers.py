#
# @lc app=leetcode.cn id=2178 lang=python3
# @lcpr version=30204
#
# [2178] 拆分成最多数目的正偶数之和
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        cur = 2
        ret = []
        while finalSum >= cur:
            ret.append(cur)
            finalSum -= cur
            cur += 2
        ret[-1] += finalSum
        return ret


# @lc code=end
assert Solution().maximumEvenSplit(28) == [2, 4, 6,16]
assert Solution().maximumEvenSplit(12) == [2, 4, 6]


#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 28\n
# @lcpr case=end

#
