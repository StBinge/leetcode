#
# @lc app=leetcode.cn id=1061 lang=python3
#
# [1061] 按字典序排列最小的等效字符串
#

# @lc code=start
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        p=list(range(26))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        def connect(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            if x<y:
                p[y]=x
            else:
                p[x]=y
        
        _ord=lambda ch:ord(ch)-ord('a')

        for c1,c2 in zip(s1,s2):
            connect(_ord(c1),_ord(c2))
        ret=['']*len(baseStr)
        for i,c in enumerate(baseStr):
            mi=find(_ord(c))
            ret[i]=chr(ord('a')+mi)
        return ''.join(ret)
# @lc code=end
assert Solution().smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode")=='aauaaaaada'
assert Solution().smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold")=='hdld'
assert Solution().smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")=='makkek'
