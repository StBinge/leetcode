#
# @lc app=leetcode.cn id=1967 lang=python3
# @lcpr version=30204
#
# [1967] 作为子字符串出现在单词中的字符串数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(word.find(p)>=0 for p in patterns)
# @lc code=end



#
# @lcpr case=start
# ["a","abc","bc","d"]\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c"]\n"aaaaabbbbb"\n
# @lcpr case=end

# @lcpr case=start
# ["a","a","a"]\n"ab"\n
# @lcpr case=end

#

