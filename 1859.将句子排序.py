#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split(' ')
        ret=['']*len(words)
        for word in words:
            ret[int(word[-1])-1]=word[:-1]
        return ' '.join(ret)
# @lc code=end
assert Solution().sortSentence("is2 sentence4 This1 a3")=="This is a sentence"
