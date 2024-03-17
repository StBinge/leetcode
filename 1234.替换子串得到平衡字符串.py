#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#
from sbw import *
# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        L=len(s)
        avg=L//4
        cnt=Counter(s)
        def valid():
            return cnt['Q']<=avg and cnt['W']<=avg and cnt['E']<=avg and cnt['R']<=avg

        if valid():
            return 0
        r=0
        ret=L
        for l,c in enumerate(s):
            while r<L and not valid():
                cnt[s[r]]-=1
                r+=1
            if not valid():
                break
            ret=min(ret,r-l)
            cnt[c]+=1
        return ret
# @lc code=end
assert Solution().balancedString('WQWRQQQW')==3
assert Solution().balancedString('QQQQ')==3
assert Solution().balancedString('QQQW')==2
assert Solution().balancedString('QQWE')==1
assert Solution().balancedString('QWER')==0
