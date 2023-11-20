#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#

# @lc code=start
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:

        idx=0

        L=len(expression)
        x,y=0,1
        sign=1

        while idx<L:
            if expression[idx]=='+' or expression[idx]=='-':           
                sign=1 if expression[idx]=='+' else -1
                idx+=1
            else:
                x1=0
                while expression[idx].isnumeric():
                    x1=x1*10+int(expression[idx])
                    idx+=1
                x1*=sign
                idx+=1
                y1=0
                while idx<L and expression[idx].isnumeric():
                    y1=y1*10+int(expression[idx])
                    idx+=1
                x=x*y1+x1*y
                y*=y1

        if x==0:
            return '0/1'
        g=math.gcd(abs(x),y)
        return f'{x//g}/{y//g}'



# @lc code=end

assert Solution().fractionAddition("-1/2+1/2+1/3")=='1/3'
assert Solution().fractionAddition("-1/2+1/2")=='0/1'
assert Solution().fractionAddition("1/3-1/2")=='-1/6'