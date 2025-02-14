#
# @lc app=leetcode.cn id=3407 lang=python3
# @lcpr version=30204
#
# [3407] 子字符串匹配模式
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split("*")
        if not left:
            return s.find(right) != -1
        idx = s.find(left)
        if idx == -1:
            return False
        if not right:
            return True
        return s.find(right, idx + len(left)) != -1


# @lc code=end
assert Solution().hasMatch("ckckkk", "ck*kc") == False
assert Solution().hasMatch("ojjju", "*o")
assert Solution().hasMatch("tokk", "t*t") == False
assert Solution().hasMatch("luck", "u*")


#
# @lcpr case=start
# "leetcode"\n"ee*e"\n
# @lcpr case=end

# @lcpr case=start
# "car"\n"c*v"\n
# @lcpr case=end

# @lcpr case=start
# "luck"\n"u*"\n
# @lcpr case=end

#
