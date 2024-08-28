#
# @lc app=leetcode.cn id=1957 lang=python3
# @lcpr version=30204
#
# [1957] 删除字符使字符串变好
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        return s[:2]+''.join(ch for idx,ch in enumerate(s[2:],2) if not (s[idx-2] == s[idx-1]==s[idx]))
# @lc code=end
assert Solution().makeFancyString('aab')=='aab'
assert Solution().makeFancyString('aaabaaaa')=='aabaa'
assert Solution().makeFancyString('leeetcode')=='leetcode'


#
# @lcpr case=start
# "leeetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aaabaaaa"\n
# @lcpr case=end

# @lcpr case=start
# "aab"\n
# @lcpr case=end

#

