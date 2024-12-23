#
# @lc app=leetcode.cn id=2942 lang=python3
# @lcpr version=30204
#
# [2942] 查找包含给定字符的单词
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,word in enumerate(words) if x in word]
# @lc code=end



#
# @lcpr case=start
# ["leet","code"]\n"e"\n
# @lcpr case=end

# @lcpr case=start
# ["abc","bcd","aaaa","cbc"]\n"a"\n
# @lcpr case=end

# @lcpr case=start
# ["abc","bcd","aaaa","cbc"]\n"z"\n
# @lcpr case=end

#

