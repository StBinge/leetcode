#
# @lc app=leetcode.cn id=2273 lang=python3
# @lcpr version=30204
#
# [2273] 移除字母异位词后的结果数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret=[]
        for word in words:
            if not ret or sorted(ret[-1])!=sorted(word):
                ret.append(word)
        return ret
# @lc code=end
assert Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"])==["abba","cd"]


#
# @lcpr case=start
# ["abba","baba","bbaa","cd","cd"]\n
# @lcpr case=end

# @lcpr case=start
# ["a","b","c","d","e"]\n
# @lcpr case=end

#

