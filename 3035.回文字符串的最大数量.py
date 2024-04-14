#
# @lc app=leetcode.cn id=3035 lang=python3
#
# [3035] 回文字符串的最大数量
#
from sbw import *
# @lc code=start
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        chars=defaultdict(int)
        for word in words:
            for ch in word:
                chars[ch]+=1
        
        single_chars=sum(v&1 for v in chars.values())
        if single_chars==0:
            return len(words)
        odd_words=sum(len(word)&1 for word in words)
        if single_chars<=odd_words:
            return len(words)
        
        words.sort(key=len,reverse=True)
        ret=len(words)
        single_chars-=odd_words
        for w in words:
            l=len(w)//2*2
            
            single_chars-=l
            ret-=1
            if single_chars<=0:
                return ret

        
# @lc code=end
assert Solution().maxPalindromesAfterOperations(["cd","ef","a"])==1
assert Solution().maxPalindromesAfterOperations(["a","bbb","ba"])==3
assert Solution().maxPalindromesAfterOperations(["abc","ab"])==2
assert Solution().maxPalindromesAfterOperations(["abbb","ba","aa"])==3
