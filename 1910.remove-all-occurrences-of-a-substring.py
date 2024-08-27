#
# @lc app=leetcode.cn id=1910 lang=python3
# @lcpr version=30204
#
# [1910] 删除一个字符串中所有出现的给定子字符串
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        M=len(part)
        next=[0]*M
        j=0
        for i in range(1,M):
            while j and part[i]!=part[j]:
                j=next[j-1]
            if part[i]==part[j]:
                j+=1
            next[i]=j
        
        # cache={}
        # cache[-1]=0
        N=len(s)
        j=0
        ret=[]
        pres=[0]
        for i in range(N):
            ret.append(s[i])
            j=pres[-1]
            while j and s[i]!=part[j]:
                j=next[j-1]
            if s[i]==part[j]:
                j+=1
            pres.append(j)
            if j==M:
                ret=ret[:-M]
                pres=pres[:-M]

        return ''.join(ret)

# @lc code=end
assert Solution().removeOccurrences(s = "eemckxmckx", part = "emckx")==''
assert Solution().removeOccurrences(s = "axxxxyyyyb", part = "xy")=='ab'
assert Solution().removeOccurrences(s = "daabcbaabcbc", part = "abc")=='dab'


#
# @lcpr case=start
# "daabcbaabcbc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "axxxxyyyyb"\n"xy"\n
# @lcpr case=end

#

