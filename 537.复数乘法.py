#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num:str):
            left,right=num.split('+')
            real=int(left)
            image=int(right[:-1])
            return real,image
        r1,i1=parse(num1)
        r2,i2=parse(num2)
        real=r1*r2-i1*i2
        image=r1*i2+r2*i1
        return f'{real}+{image}i'
# @lc code=end

r= Solution().complexNumberMultiply('1+1i','1+1i')
assert r=='0+2i'

r= Solution().complexNumberMultiply('1+-1i','1+-1i')
assert r=='0+-2i'