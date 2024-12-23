#
# @lc app=leetcode.cn id=3223 lang=python3
# @lcpr version=30204
#
# [3223] 操作后字符串的最短长度
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        cnt=Counter(s)
        return sum((v-1)%2 +1 for v in cnt.values())
# @lc code=end
assert Solution().minimumLength('abaacbcbb')==5


#
# @lcpr case=start
# "abaacbcbb"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

