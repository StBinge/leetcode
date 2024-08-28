#
# @lc app=leetcode.cn id=2124 lang=python3
# @lcpr version=30204
#
# [2124] 检查是否所有 A 都在 B 之前
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        b=False
        for ch in s:
            if ch=='b':
                b=True
            elif b:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "aaabbb"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n
# @lcpr case=end

# @lcpr case=start
# "bbb"\n
# @lcpr case=end

#

