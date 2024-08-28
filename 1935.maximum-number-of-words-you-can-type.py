#
# @lc app=leetcode.cn id=1935 lang=python3
# @lcpr version=30204
#
# [1935] 可以输入的最大单词数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ret = 0
        idx = 0
        invalid = set(brokenLetters)
        N = len(text)
        while idx < N:
            valid = True
            while idx < N and text[idx] != " ":
                if text[idx] in invalid:
                    valid = False
                    break
                idx += 1
            if valid:
                ret += 1
            else:
                while idx < N and text[idx] != " ":
                    idx += 1
            idx += 1
        return ret


# @lc code=end
assert Solution().canBeTypedWords(text="leet code", brokenLetters="e") == 0
assert Solution().canBeTypedWords(text="leet code", brokenLetters="lt") == 1
assert Solution().canBeTypedWords("hello world", "ad") == 1


#
# @lcpr case=start
# "hello world"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "leet code"\n"lt"\n
# @lcpr case=end

# @lcpr case=start
# "leet code"\n"e"\n
# @lcpr case=end

#
