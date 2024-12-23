#
# @lc app=leetcode.cn id=2287 lang=python3
# @lcpr version=30204
#
# [2287] 重排字符形成目标字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cnt=Counter(s)
        cnt2=Counter(target)
        return min(cnt[k]//cnt2[k] for k in cnt2)
# @lc code=end



#
# @lcpr case=start
# "ilovecodingonleetcode"\n"code"\n
# @lcpr case=end

# @lcpr case=start
# "abcba"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abbaccaddaeea"\n"aaaaa"\n
# @lcpr case=end

#

