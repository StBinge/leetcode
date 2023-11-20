#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        t=['^','#']
        for c in s:
            t.append(c)
            t.append('#')
        t.append('$')
        f=[1]*len(t)
        iMax,rMax=0,0
        ret=0
        for i in range(2,len(t)-2):
            if i<rMax:
                f[i]=min(f[2*iMax-i],rMax-i+1)
            # f[i]+=1
            while t[i-f[i]]==t[i+f[i]]:
                f[i]+=1
            # f[i]-=1
            ret+=f[i]//2
        return ret


# @lc code=end
assert Solution().countSubstrings('abc') == 3
assert Solution().countSubstrings('aaa') == 6
