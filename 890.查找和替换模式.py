#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#
from sbw import *
# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        L=len(pattern)
        def is_map(word:str):
            nonlocal L
            chars={}
            reversed_chars={}
            for i in range(L):
                if word[i] not in chars and pattern[i] not in reversed_chars:
                    chars[word[i]]=pattern[i]
                    reversed_chars[pattern[i]]=word[i]
                elif word[i] in chars and chars[word[i]]!=pattern[i]:
                    return False
                elif pattern[i] in reversed_chars and word[i]!=reversed_chars[pattern[i]]:
                    return False
            return True
        ret=[]
        for word in words:
            if is_map(word):
                ret.append(word)
        return ret
# @lc code=end
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
ret=["mee","aqq"]
assert Solution().findAndReplacePattern(words,pattern)==ret