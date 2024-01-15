#
# @lc app=leetcode.cn id=1177 lang=python3
#
# [1177] 构建回文串检测
#
from sbw import *
# @lc code=start
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        L=len(s)
        count=[0]*(L+1)
        for i in range(L):
            count[i+1]=count[i] ^ (1<<(ord(s[i])-ord('a')))
        ret=[]
        for l,r,k in queries:
            mask=count[r+1] ^ count[l]
            cnt=0
            while mask>0:
                cnt+=1
                mask &= mask-1
            ret.append(cnt<=2*k+1)
        return ret
# @lc code=end
assert Solution().canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]])==eval_list_str('[true,false,false,true,true]')
