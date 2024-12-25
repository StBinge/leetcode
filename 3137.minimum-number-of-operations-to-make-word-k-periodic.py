#
# @lc app=leetcode.cn id=3137 lang=python3
# @lcpr version=30204
#
# [3137] K 周期字符串需要的最少操作次数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        N = len(word)
        cnt = Counter([word[i : i  + k] for i in range(0, N, k)])
        return N // k - max(cnt.values())


# @lc code=end
assert Solution().minimumOperationsToMakeKPeriodic(word="xtxt", k=2) == 0
assert Solution().minimumOperationsToMakeKPeriodic(word="leetcoleet", k=2) == 3
assert Solution().minimumOperationsToMakeKPeriodic(word="leetcodeleet", k=4) == 1


#
# @lcpr case=start
# "leetcodeleet"\n4\n
# @lcpr case=end

# @lcpr case=start
# "leetcoleet"\n2\n
# @lcpr case=end

#
