#
# @lc app=leetcode.cn id=2278 lang=python3
# @lcpr version=30204
#
# [2278] 字母在字符串中的百分比
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt=s.count(letter)
        return int(cnt*100/len(s))

# @lc code=end



#
# @lcpr case=start
# "foobar"\n"o"\n
# @lcpr case=end

# @lcpr case=start
# "jjjj"\n"k"\n
# @lcpr case=end

#

