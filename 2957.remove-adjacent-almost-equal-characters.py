#
# @lc app=leetcode.cn id=2957 lang=python3
# @lcpr version=30204
#
# [2957] 消除相邻近似相等字符
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        precode = 0
        ret = 0
        for ch in word:
            code = ord(ch)
            if abs(code - precode) <= 1:
                ret += 1
                precode = 0
            else:
                precode = code
        return ret


# @lc code=end
assert Solution().removeAlmostEqualCharacters("zyxyxyz") == 3
assert Solution().removeAlmostEqualCharacters("abddez") == 2
assert Solution().removeAlmostEqualCharacters("aaaaa") == 2


#
# @lcpr case=start
# "aaaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abddez"\n
# @lcpr case=end

# @lcpr case=start
# "zyxyxyz"\n
# @lcpr case=end

#
