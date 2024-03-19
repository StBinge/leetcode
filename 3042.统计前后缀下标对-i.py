#
# @lc app=leetcode.cn id=3042 lang=python3
#
# [3042] 统计前后缀下标对 I
#
from sbw import *
# @lc code=start
class Node:
    def __init__(self) -> None:
        self.slots={}
        self.cnt=0
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def calc_z(word:str):
            L=len(word)
            z=[0]*L
            l=0
            r=0
            for i in range(1,L):
                if i<=r:
                    z[i]=min(r-i,z[i-l])
                while i+z[i]<L and word[i+z[i]]==word[z[i]]:
                    z[i]+=1
                if i+z[i]>r:
                    r=i+z[i]
                    l=i
            z[0]=L
            return z

        ret=0
        root=Node()
        for w in words:
            cur=root
            z=calc_z(w)
            for i,ch in enumerate(w):
                cur=cur.slots.setdefault(ch,Node())
                if z[-1-i]==i+1:
                    ret+=cur.cnt
            cur.cnt+=1
        return ret
# @lc code=end
assert Solution().countPrefixSuffixPairs(words = ["abab","ab"])==0
assert Solution().countPrefixSuffixPairs(words = ["pa","papa","ma","mama"])==2
assert Solution().countPrefixSuffixPairs(words = ["a","aba","ababa","aa"])==4
