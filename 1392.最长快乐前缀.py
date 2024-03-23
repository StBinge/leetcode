#
# @lc app=leetcode.cn id=1392 lang=python3
#
# [1392] 最长快乐前缀
#

# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        L=len(s)
  
        pre1,pre2=0,0
        suf1,suf2=0,0
        mod1=10**9+7
        mod2=10**9+101
        orda=ord('a')
        ret=-1
        base=27
        mul1=1
        mul2=1
        for i in range(L-1):
            pre1=((ord(s[i])-orda)+pre1*base)%mod1
            pre2=((ord(s[i])-orda)+pre2*base)%mod2
            suf1=((ord(s[L-1-i])-orda)*mul1+suf1)%mod1
            suf2=((ord(s[L-1-i])-orda)*mul2+suf2)%mod2
            if pre1==suf1 and pre2==suf2:
                ret=i
            mul1=(mul1*base)%mod1
            mul2=(mul2*base)%mod2
        return s[:ret+1]

            
# @lc code=end
assert Solution().longestPrefix('acccbaaacccbaac')=='ac'
assert Solution().longestPrefix('bba')==''
assert Solution().longestPrefix('a')==''
assert Solution().longestPrefix('level')=='l'
assert Solution().longestPrefix('ababab')=='abab'
