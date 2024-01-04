#
# @lc app=leetcode.cn id=1048 lang=python3
#
# [1048] 最长字符串链
#
from sbw import *
# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length_cnt={}
        for i,w in enumerate(words):
            length_cnt.setdefault(len(w),[]).append(i)
        
        @cache
        def match(prev,next):
            w1,w2=words(prev),words[next]
            idx=0
            mis=0
            for c in w1:
                if c==w2[idx]:
                    idx+=1
                else:
                    mis+=1
                    if mis>1:
                        return False
            return True
        @cache
        def dfs(wid):
            l=len(words[wid])
            ret=0
            for nxt in length_cnt.get(l+1,[]):
                if match(wid,nxt):
                    ret=max(ret,dfs(nxt)+1)
            return ret
        ret=0
        for i in range(len(words)):
            ret=max(ret,dfs(i))
        return ret
# @lc code=end
words = ["a","b","ba","bca","bda","bdca"]
assert Solution().longestStrChain(words)==4
