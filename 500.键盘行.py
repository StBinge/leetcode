#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
from typing import List
# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line_id={}
        chars=['qwertyuiop','asdfghjkl','zxcvbnm']
        for i in range(3):
            for ch in chars[i]:
                line_id[ch]=i
        
        ret=[]
        for word in words:
            idx=line_id[word[0].lower()]
            for ch in word[1:]:
                if idx!=line_id[ch.lower()]:
                    break
            else:
                ret.append(word)
        return ret
# @lc code=end
words = ["Hello","Alaska","Dad","Peace"]
print(Solution().findWords(words))

words = ["omk"]
print(Solution().findWords(words))

words = ["adsdf","sfd"]
print(Solution().findWords(words))
