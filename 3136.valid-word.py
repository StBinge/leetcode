#
# @lc app=leetcode.cn id=3136 lang=python3
# @lcpr version=30204
#
# [3136] 有效单词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        has_vow=has_no=False
        for ch in word.lower():
            if ch.isnumeric():
                continue
            elif ch.isalpha():
                if ch in 'aeiou':
                    has_vow=True
                else:
                    has_no=True
            else:
                return False
        return has_vow and has_no
# @lc code=end



#
# @lcpr case=start
# "234Adas"\n
# @lcpr case=end

# @lcpr case=start
# "b3"\n
# @lcpr case=end

# @lcpr case=start
# "a3$e"\n
# @lcpr case=end

#

