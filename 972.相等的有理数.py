#
# @lc app=leetcode.cn id=972 lang=python3
#
# [972] 相等的有理数
#
from sbw import *
# @lc code=start

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(s:str):
            L=len(s)
            idx=0
            int_part=0
            while idx<L and s[idx]!='.':
                int_part=int_part*10+int(s[idx])
                idx+=1
            idx+=1
            frac_part=0
            scale=1
            while idx<L and s[idx]!='(':
                frac_part=frac_part*10+int(s[idx])
                idx+=1
                scale*=10
            idx+=1
            repeat_part=[]
            while idx<L and s[idx]!=')':
                repeat_part.append(int(s[idx]))
                idx+=1
            
            l=len(repeat_part)
            for i in range(1,l//2+1):
                if l%i==0 and repeat_part[:i]*(l//i)==repeat_part:
                    repeat_part=repeat_part[:i]
                    break
            r=0
            l=len(repeat_part)
            for n in repeat_part:
                r=r*10+n
            if r==9:
                r=0
                frac_part+=1
                if frac_part==scale:
                    frac_part=0
                    int_part+=1
            else:
                high=10**(l-1)
                while frac_part and frac_part % 10==r%10:
                    frac_part//=10
                    r=(r%10)*high+r//10
                    scale//=10
            while frac_part and scale and frac_part%10==0 and scale%10==0:
                frac_part//=10
                scale//=10

            if r==0:
                l==0
            return int_part,[frac_part,scale],[r,l]
        
        sp=parse(s)
        st=parse(t)
        if sp[0]!=st[0]:
            return False
    
        if sp[1]!=st[1] and (sp[2][0]!=0 and st[2][0]!=0):
            return False
        if sp[2][0]!=st[2][0] or sp[2][0]*st[2][1]!=sp[2][1]*st[2][0]:
            return False
        return True
# @lc code=end
s = "0.9(9)"
t = "1."
assert Solution().isRationalEqual(s,t)

s="1.(1)"
t="1.0(1)"
assert Solution().isRationalEqual(s,t)==False

s = "4432.19(9)"
t = "4432.2(0)"
assert Solution().isRationalEqual(s,t)

s = "2.(2)"
t = "2"
assert Solution().isRationalEqual(s,t)==False



s = "0.(52)"
t = "0.5(25)"
assert Solution().isRationalEqual(s,t)

s = "0.1666(6)"
t = "0.166(66)"
assert Solution().isRationalEqual(s,t)