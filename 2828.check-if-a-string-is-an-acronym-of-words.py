#
# @lc app=leetcode.cn id=2828 lang=python3
# @lcpr version=30204
#
# [2828] 判别首字母缩略词
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return len(words)==len(s) and all(word[0]==ch for word,ch in zip(words,s))
# @lc code=end



#
# @lcpr case=start
# ["alice","bob","charlie"]\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# ["an","apple"]\n"a"\n
# @lcpr case=end

# @lcpr case=start
# ["never","gonna","give","up","on","you"]\n"ngguoy"\n
# @lcpr case=end

#

