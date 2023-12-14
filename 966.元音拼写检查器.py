#
# @lc app=leetcode.cn id=966 lang=python3
#
# [966] 元音拼写检查器
#
from sbw import *
# @lc code=start




    
    
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        same=set(wordlist)
        nocase={}
        novow={}
        def devow(word:str):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        for word in wordlist:
            low=word.lower()
            nocase.setdefault(low,word)
            novow.setdefault(devow(low),word)
        
        ret=[]
        for query in queries:
            if query in same:
                ret.append(query)
                continue
            low=query.lower()
            if low in nocase:
                ret.append(nocase[low])
                continue
            dv=devow(low)
            if dv in novow:
                ret.append(novow[dv])
                continue
            ret.append('')
        return ret
# @lc code=end
wordlist = ["yellow"]
queries = ["YellOw"]
ret=["yellow"]
assert Solution().spellchecker(wordlist,queries)==ret

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
ret=["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
assert Solution().spellchecker(wordlist,queries)==ret
