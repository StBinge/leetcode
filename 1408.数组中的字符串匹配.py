#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#
from sbw import *
# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret=[]
        words.sort(key=len,reverse=True)
        for i,word in enumerate(words):
            for j in range(i):
                if word in words[j]:
                    ret.append(word)
                    break
        return ret
# @lc code=end
assert sorted(Solution().stringMatching(["mass","as","hero","superhero"]))==["as","hero"]
