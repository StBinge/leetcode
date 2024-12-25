#
# @lc app=leetcode.cn id=2186 lang=python3
# @lcpr version=30204
#
# [2186] 制造字母异位词的最小步骤数 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt=Counter(s)
        for ch in t:
            cnt[ch]-=1
        return sum(abs(v) for v in cnt.values())
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n"coats"\n
# @lcpr case=end

# @lcpr case=start
# "night"\n"thing"\n
# @lcpr case=end

#

