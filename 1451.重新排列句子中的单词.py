#
# @lc app=leetcode.cn id=1451 lang=python3
#
# [1451] 重新排列句子中的单词
#

# @lc code=start
class Solution:
    def arrangeWords(self, text: str) -> str:
        words=text.split(' ')
        words[0]=words[0].lower()
        words.sort(key=len)
        words[0]=words[0].title()
        return ' '.join(words)
# @lc code=end
assert Solution().arrangeWords("Keep calm and code on")=="On and keep calm code"
assert Solution().arrangeWords("Leetcode is cool")=="Is cool leetcode"
