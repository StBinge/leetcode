#
# @lc app=leetcode.cn id=2114 lang=python3
# @lcpr version=30204
#
# [2114] 句子中的最多单词数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(' ') for s in sentences)+1
# @lc code=end



#
# @lcpr case=start
# ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]\n
# @lcpr case=end

# @lcpr case=start
# ["please wait", "continue to fight", "continue to win"]\n
# @lcpr case=end

#

