#
# @lc app=leetcode.cn id=1961 lang=python3
# @lcpr version=30204
#
# [1961] 检查字符串是否为数组前缀
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        idx=0
        N=len(s)
        for word in words:
            for ch in word:
                if idx ==N or s[idx]!=ch:
                    return False
                idx+=1

            else:
                if idx==N:
                    return True
        return False
# @lc code=end
assert not Solution().isPrefixString("a",["aa","aaaa","banana"])
assert not Solution().isPrefixString(s = "iloveleetcode", words = ["apples","i","love","leetcode"])
assert Solution().isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"])


#
# @lcpr case=start
# "iloveleetcode"\n["i","love","leetcode","apples"]\n
# @lcpr case=end

# @lcpr case=start
# "iloveleetcode"\n["apples","i","love","leetcode"]\n
# @lcpr case=end

#

