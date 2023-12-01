#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#

# @lc code=start
from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        s,t=[],[]
        for x,y in zip(s1,s2):
            if x!=y:
                s.append(x)
                t.append(y)
        n=len(s)
        if n==0:
            return 0
        ret=n-1
        def dfs(idx,cost):
            nonlocal n,ret
            if cost>ret:
                return
            while idx<n and s[idx]==t[idx]:
                idx+=1
            if idx==n:
                ret=cost
                return
            diff=sum(s[i]!=t[i] for i in range(idx,n))
            min_cost=cost+(diff+1)//2
            if min_cost>=ret:
                return
            for j in range(idx+1,n):
                if s[j]==t[idx]:
                    s[j],s[idx]=s[idx],s[j]
                    dfs(idx+1,cost+1)
                    s[j],s[idx]=s[idx],s[j]

        dfs(0,0)
        return ret
                
# @lc code=end
s1 = "abc"
s2 = "bca"
ret=2
assert Solution().kSimilarity(s1,s2)==ret

s1 = "ab"
s2 = "ba"
ret=1
assert Solution().kSimilarity(s1,s2)==ret
