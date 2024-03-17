#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#
from sbw import *
# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        L=len(s)
        p=list(range(L))

        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]

        def connect(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            # if x>y:
            #     x,y=y,x
            p[y]=x

        for p1,p2 in pairs:
            connect(p1,p2)
        
        memo={}
        for i in range(L):
            d=memo.setdefault(find(i),defaultdict(int))
            d[s[i]]+=1
        
        ret=[]
        orda=ord('a')
        for i in range(L):
            pa=find(i)
            d=memo[pa]
            if len(d)==1:
                ret.append(s[i])
                continue
            for i in range(26):
                ch=chr(orda+i)
                if d[ch]>0:
                    ret.append(ch)
                    d[ch]-=1
                    break
        return ''.join(ret)

# @lc code=end
assert Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])=='abcd'
assert Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])=='bacd'
