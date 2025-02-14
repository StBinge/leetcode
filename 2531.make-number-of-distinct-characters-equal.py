#
# @lc app=leetcode.cn id=2531 lang=python3
# @lcpr version=30204
#
# [2531] 使字符串中不同字符的数目相等
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        if len(cnt1) > len(cnt2):
            cnt1, cnt2 = cnt2, cnt1
        c1, c2 = len(cnt1), len(cnt2)
        if c2 - c1 > 2:
            return False

        for k1 in cnt1:
            rm1 = cnt1[k1] == 1
            add2 = k1 not in cnt2
            for k2 in cnt2:
                if k1 == k2:
                    if c1 == c2:
                        return True
                    continue
                rm2 = cnt2[k2] == 1
                add1 = k2 not in cnt1
                if c1 - rm1 + add1 == c2 - rm2 + add2:
                    return True
        return False


# @lc code=end
assert Solution().isItPossible(word1 = "abcde", word2 = "fghij") 
assert Solution().isItPossible(word1 = "abcc", word2 = "aab") 
assert Solution().isItPossible(word1="ac", word2="b") == False


#
# @lcpr case=start
# "ac"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "abcc"\n"aab"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"fghij"\n
# @lcpr case=end

#
