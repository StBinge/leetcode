#
# @lc app=leetcode.cn id=2734 lang=python3
# @lcpr version=30204
#
# [2734] 执行子串操作后的字典序最小字符串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestString(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] != "a":
                ret = s[:i]
                for j in range(i, len(s)):
                    if s[j] == "a":
                        ret += s[j:]
                        break
                    ret += chr(ord(s[j]) - 1)
                return ret
        return s[:-1] + "z"


# @lc code=end
assert Solution().smallestString("baa") == "aaa"

#
# @lcpr case=start
# "cbabc"\n
# @lcpr case=end

# @lcpr case=start
# "acbbc"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

#
