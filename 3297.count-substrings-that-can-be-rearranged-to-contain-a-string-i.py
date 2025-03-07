#
# @lc app=leetcode.cn id=3297 lang=python3
# @lcpr version=30204
#
# [3297] 统计重新排列后包含另一个字符串的子字符串数目 I
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1)<len(word2):
            return 0
        cnt = Counter(word2)
        ret = left = 0
        not_valid = len(cnt)
        for ch in word1:
            cnt[ch] -= 1
            if cnt[ch] == 0:
                not_valid -= 1
            while not_valid == 0:
                cnt[word1[left]] += 1
                if cnt[word1[left]] == 1:
                    not_valid += 1
                left += 1
            ret += left
        return ret


# @lc code=end
assert Solution().validSubstringCount(word1 = "abcabc", word2 = "aaabc") == 0
assert Solution().validSubstringCount(word1 = "abcabc", word2 = "abc") == 10
assert Solution().validSubstringCount(word1="bcca", word2="abc") == 1


#
# @lcpr case=start
# "bcca"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abcabc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abcabc"\n"aaabc"\n
# @lcpr case=end

#
