#
# @lc app=leetcode.cn id=2207 lang=python3
# @lcpr version=30204
#
# [2207] 字符串中最多数目的子序列
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p1, p2 = pattern
        if p1 == p2:
            cnt = text.count(p1) + 1
            return cnt * (cnt - 1) // 2
        cnt1 = 0
        cnt2 = 0
        ret=0
        for ch in text:
            if ch == p1:
                cnt1+=1
            elif ch==p2:
                ret+=cnt1
                cnt2+=1
        return ret+max(cnt1,cnt2)


# @lc code=end
assert Solution().maximumSubsequenceCount("y", "yy") == 1
assert (
    Solution().maximumSubsequenceCount("iekbksdsmuuzwxbpmcngsfkjvpzuknqguzvzik", "mp")
    == 5
)


#
# @lcpr case=start
# "abdcdbc"\n"ac"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n"ab"\n
# @lcpr case=end

#
