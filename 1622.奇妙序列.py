#
# @lc app=leetcode.cn id=1622 lang=python3
#
# [1622] 奇妙序列
#
from sbw import *
# @lc code=start
class Fancy:

    def __init__(self):
        self.v=[]
        self.a=[1]
        self.b=[0]

    def quickmul(self,x,y):
        return pow(x,y,10**9+7)

    def inv(self,x):
        return self.quickmul(x,10**9+5)

    def append(self, val: int) -> None:
        self.v.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1]=(self.b[-1]+inc)%(10**9+7)

    def multAll(self, m: int) -> None:
        self.a[-1]=(self.a[-1]*m)%(10**9+7)
        self.b[-1]=(self.b[-1]*m)%(10**9+7)

    def getIndex(self, idx: int) -> int:
        if idx>=len(self.v):
            return -1
        a0=self.inv(self.a[idx])*self.a[-1]
        b0=self.b[-1]-self.b[idx]*a0
        return (self.v[idx]*a0+b0)%(10**9+7)



# @lc code=end

fancy = Fancy()#
assert fancy.getIndex(0)==-1
fancy.append(2)#   // 奇妙序列：[2]
fancy.addAll(3)#   // 奇妙序列：[2+3] -> [5]
fancy.append(7)#   // 奇妙序列：[5, 7]
fancy.multAll(2)#  // 奇妙序列：[5*2, 7*2] -> [10, 14]
assert fancy.getIndex(0)==10# // 返回 10
fancy.addAll(3)#   // 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10)#  // 奇妙序列：[13, 17, 10]
fancy.multAll(2)#  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
assert fancy.getIndex(0) == 26 # // 返回 26
assert fancy.getIndex(1) ==34# // 返回 34
assert fancy.getIndex(2) ==20# // 返回 20