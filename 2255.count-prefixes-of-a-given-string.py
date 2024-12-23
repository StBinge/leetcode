#
# @lc app=leetcode.cn id=2255 lang=python3
# @lcpr version=30204
#
# [2255] 统计是给定字符串前缀的字符串数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)

# @lc code=end



#
# @lcpr case=start
# ["a","b","c","ab","bc","abc"]\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# ["a","a"]\n"aa"\n
# @lcpr case=end

#

