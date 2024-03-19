#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#
from sbw import *
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # n1,n2=[],[]
        n1=[]
        N=n
        while n>0:
            d=n%10
            n//=10
            if d>1:
                n1.append(1)
            elif n>0:
                n1.append(2)
                n-=1
            
        r1=0
        for d in reversed(n1):
            r1=r1*10+d
        return [r1,N-r1]
# @lc code=end
n1,n2= Solution().getNoZeroIntegers(19)
assert n1+n2==19 and str(n1).find('0')<0 and str(n2).find('0')<0
n1,n2= Solution().getNoZeroIntegers(11)
assert n1+n2==11 and str(n1).find('0')<0 and str(n2).find('0')<0
