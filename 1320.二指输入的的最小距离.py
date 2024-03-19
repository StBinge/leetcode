#
# @lc app=leetcode.cn id=1320 lang=python3
#
# [1320] 二指输入的的最小距离
#
from sbw import *
# @lc code=start
class Solution:
    def minimumDistance(self, word: str) -> int:
        L=len(word)
        def get_dis(p1,p2):
            x1,y1=p1//6,p1%6
            x2,y2=p2//6,p2%6
            return abs(x1-x2)+abs(y1-y2)
        Max=L*20
        f=[[0]*26,[Max]*26]
        ordA=ord('A')
        # ord0=ord(word[0])-ordA
        # f[ord0]=0
        for i in range(1,L):
            pre=ord(word[i-1])-ordA
            cur=ord(word[i])-ordA
            dis=get_dis(pre,cur)
            for j in range(26):
                f[1][j]=f[0][j]+dis
                if pre==j:
                    for k in range(26):
                        dk=get_dis(k,cur)
                        f[1][j]=min(f[1][j],f[0][k]+dk)
            f[0],f[1]=f[1],f[0]
        return min(f[0])

# @lc code=end
assert Solution().minimumDistance('HAPPY')==6
assert Solution().minimumDistance('CAKE')==3
