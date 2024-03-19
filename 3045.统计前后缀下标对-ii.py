#
# @lc app=leetcode.cn id=3045 lang=python3
#
# [3045] 统计前后缀下标对 II
#
from sbw import *
# @lc code=start
class Node:
    def __init__(self) -> None:
        self.slots={}
        self.cnt=0
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def Z(s:str):
            L=len(s)
            z=[0]*L
            l=r=0
            for i in range(1,L):
                if i<=r:
                    z[i]=min(z[i-l],r-i+1)
                while i+z[i]<L and s[z[i]]==s[i+z[i]]:
                    z[i]+=1
                if r<i+z[i]:
                    r=i+z[i]-1
                    l=i
            z[0]=L
            return z
        root=Node()
        ret=0
        for word in words:
            cur=root
            z=Z(word)
   
            for i,c in enumerate(word):
                cur=cur.slots.setdefault(c,Node())
                if z[-1-i]==i+1:
                    ret+=cur.cnt
            cur.cnt+=1
        return ret
# @lc code=end
assert Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"])==4
assert Solution().countPrefixSuffixPairs(["a",'a'])==1
