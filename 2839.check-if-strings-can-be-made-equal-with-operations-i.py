#
# @lc app=leetcode.cn id=2839 lang=python3
# @lcpr version=30204
#
# [2839] 判断通过操作能否让字符串相等 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return sorted(s1[0::2])==sorted(s2[0::2]) and sorted(s1[1::2]) == sorted(s2[1::2])

# @lc code=end



#
# @lcpr case=start
# "abcd"\n"cdab"\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"dacb"\n
# @lcpr case=end

#

