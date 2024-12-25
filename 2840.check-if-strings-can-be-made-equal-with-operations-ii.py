#
# @lc app=leetcode.cn id=2840 lang=python3
# @lcpr version=30204
#
# [2840] 判断通过操作能否让字符串相等 II
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(
            s2[1::2]
        )


# @lc code=end


#
# @lcpr case=start
# "abcdba"\n"cabdab"\n
# @lcpr case=end

# @lcpr case=start
# "abe"\n"bea"\n
# @lcpr case=end

#
