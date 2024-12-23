#
# @lc app=leetcode.cn id=2716 lang=python3
# @lcpr version=30204
#
# [2716] 最小化字符串长度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
# @lc code=end



#
# @lcpr case=start
# "aaabc"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

# @lcpr case=start
# "dddaaa"\n
# @lcpr case=end

#

