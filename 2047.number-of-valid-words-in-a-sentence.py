#
# @lc app=leetcode.cn id=2047 lang=python3
# @lcpr version=30204
#
# [2047] 句子中的有效单词数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        ret = 0
        idx = 0
        N = len(sentence)

        slash = False
        punc = False
        token = False

        def jump():
            nonlocal idx, punc, slash, token
            while idx < N and sentence[idx] != " ":
                idx += 1
            idx += 1
            slash = False
            punc = False
            token = False

        while idx < N:
            ch = sentence[idx]
            if ch.isnumeric():
                jump()
            elif ch == "-":
                if (
                    not slash
                    and idx > 0
                    and sentence[idx - 1].isalpha()
                    and idx + 1 < N
                    and sentence[idx + 1].isalpha()
                ):
                    idx += 2
                    slash = True
                else:
                    jump()
            elif ch in "!.,":
                if not punc and (idx + 1 == N or sentence[idx + 1] == " "):
                    punc = True
                    token = True
                    idx += 1
                else:
                    jump()
            elif ch == " ":
                if token:
                    ret += 1
                jump()
            else:
                token = True
                idx += 1
        if token:
            ret += 1
        return ret


# @lc code=end
assert Solution().countValidWords(".") == 1
assert (
    Solution().countValidWords(
        "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
    )
    == 6
)
assert Solution().countValidWords("alice and  bob are playing stone-game10") == 5
assert Solution().countValidWords("!this  1-s b8d!") == 0
assert Solution().countValidWords("cat and  dog") == 3


#
# @lcpr case=start
# "cat and  dog"\n
# @lcpr case=end

# @lcpr case=start
# "!this  1-s b8d!"\n
# @lcpr case=end

# @lcpr case=start
# "alice and  bob are playing stone-game10"\n
# @lcpr case=end

#
