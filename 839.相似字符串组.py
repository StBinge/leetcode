#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#
from typing import List
# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)

        w=len(strs[0])
        if w==1:
            return n
        p=list(range(n))
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        def connect(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            p[px]=py
        
        
        for i in range(n):
            for j in range(i+1,n):
                if find(i)==find(j):
                    continue

                cnt=0
                for c1,c2 in zip(strs[i],strs[j]):
                    if c1!=c2:
                        cnt+=1
                        if cnt>2:
                            break
                else:
                    connect(i,j)
        return sum(i==p[i] for i in range(n))
# @lc code=end

strs=["tars","rats","arts","star"]
assert Solution().numSimilarGroups(strs)==2
strs = ["omv","ovm"]
assert Solution().numSimilarGroups(strs)==1
