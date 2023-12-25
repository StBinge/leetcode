#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#
from sbw import *
# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p=[i for i in range(26)]
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        def connect(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            p[x]=y
        for eq in equations:
            if eq[1]=='!':
                continue
            a,b=ord(eq[0])-ord('a'),ord(eq[3])-ord('a')
            connect(a,b)
        
        for eq in equations:
            if eq[1]=='=':
                continue
            a,b=ord(eq[0])-ord('a'),ord(eq[3])-ord('a')
            if find(a)==find(b):
                return False
        return True
                

# @lc code=end
assert  Solution().equationsPossible(["c==c","b==d","x!=z"])

assert not Solution().equationsPossible(["a==b","b!=c","c==a"])

assert  Solution().equationsPossible(["a==b","b==c","a==c"])

assert not Solution().equationsPossible(["a==b","b!=a"])
assert  Solution().equationsPossible(["a==b","b==a"])
