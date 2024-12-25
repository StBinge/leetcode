#
# @lc app=leetcode.cn id=2185 lang=python3
# @lcpr version=30204
#
# [2185] 统计包含给定前缀的字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)
# @lc code=end



#
# @lcpr case=start
# ["pay","attention","practice","attend"]\n"at"\n
# @lcpr case=end

# @lcpr case=start
# ["leetcode","win","loops","success"]\n"code"\n
# @lcpr case=end

#

