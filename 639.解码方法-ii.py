#
# @lc app=leetcode.cn id=639 lang=python3
#
# [639] 解码方法 II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        Mod=10**9+7
        L=len(s)
        
        def check1(ch:str):
            if ch=='*':
                return 9
            elif ch=='0':
                return 0
            else:
                return 1
        
        def check2(c1,c2):
            if c1=='*' and c2=='*':
                return 15
            if c1=='*':
                return 2 if c2<'7' else 1
            if c2=='*':
                if c1=='1':
                    return 9
                if c1=='2':
                    return 6
                return 0
            if 9<int(c1+c2)<27:
                return 1
            return 0

        a=1
        b=check1(s[0])
        c=b
        for i in range(1,L):
            s1=check1(s[i])
            c=b*s1
            s2=check2(s[i-1],s[i])
            c+=a*s2
            c%=Mod
            a,b=b,c
        return c
# @lc code=end
assert Solution().numDecodings('104')==1
assert Solution().numDecodings('0')==0
assert Solution().numDecodings('*10*1')==99
assert Solution().numDecodings('**')==96
assert Solution().numDecodings('*1*1*0')==404
assert Solution().numDecodings('*1')==11
assert Solution().numDecodings('1*')==18
assert Solution().numDecodings('*')==9
assert Solution().numDecodings('2*')==15
