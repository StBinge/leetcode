#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#
from typing import List
# @lc code=start
# from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set=set(w.lower() for w in banned)
        counter={}
        idx=0
        L=len(paragraph)
        cnt=0
        ret=''
        while idx<L:
            while idx<L and paragraph[idx].isalpha()==False:
                idx+=1
            start=idx
            while idx<L and paragraph[idx].isalpha():
                idx+=1
            word=paragraph[start:idx].lower()
            if word in ban_set:
                continue
            counter[word]=counter.get(word,0)+1
            if counter[word]>cnt:
                cnt=counter[word]
                ret=word
        return ret
# @lc code=end
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
assert Solution().mostCommonWord(paragraph,banned)=='ball'
