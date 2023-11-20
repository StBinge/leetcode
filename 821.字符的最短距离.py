#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=len(s)
        ret=[0]*len(s)
        cid=-l
        for i,chr in enumerate(s):
            if chr==c:
                cid=i
            ret[i]=i-cid
        
        cid=2*l
        for i in range(l-1,-1,-1):
            chr=s[i]
            if chr==c:
                cid=i
            ret[i]=min(ret[i],cid-i)
        return ret
# @lc code=end
s = "loveleetcode"
c = "e"
assert Solution().shortestToChar(s,c)==[3,2,1,0,1,0,0,1,2,2,1,0]