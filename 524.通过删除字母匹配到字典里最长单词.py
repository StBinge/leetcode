#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
from typing import List
# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x),x))
        L=len(s)
        for word in dictionary:
            p1,p2=0,0
            L2=len(word)
            while p1<L and p2<L2:
                if s[p1]==word[p2]:
                    p1+=1
                    p2+=1
                else:
                    p1+=1
            if p2==L2:
                return word
        return ''
# @lc code=end
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
assert Solution().findLongestWord(s,dictionary)=='apple'
s = "abpcplea"
dictionary = ["a","b","c"]
assert Solution().findLongestWord(s,dictionary)=='a'
