#
# @lc app=leetcode.cn id=3081 lang=python3
#
# [3081] 替换字符串中的问号使分数最小
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq=[0]*26
        needs=0
        for code in s:
            if code=='?':
                needs+=1
            else:
                freq[ord(code)-ord('a')]+=1
        h=[[f,idx] for idx,f in enumerate(freq)]
        heapq.heapify(h)
        adds=[0]*26
        for i in range(needs):
            f,code=h[0]
            adds[code]+=1
            heapq.heapreplace(h,[f+1,code])

        idx=0
        ret=list(s)
        for i in range(len(s)):
            if ret[i]=='?':
                while adds[idx]==0:
                    idx+=1
                ret[i]=chr(idx+ord('a'))
                adds[idx]-=1

            
            
        return ''.join(ret)
# @lc code=end
assert Solution().minimizeStringValue('abcdefghijklmnopqrstuvwxy??')=='abcdefghijklmnopqrstuvwxyaz'
assert Solution().minimizeStringValue('a?a?')=='abac'
assert Solution().minimizeStringValue('???')=='abc'
