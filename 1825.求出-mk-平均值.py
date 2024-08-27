#
# @lc app=leetcode.cn id=1825 lang=python3
#
# [1825] 求出 MK 平均值
#
from sbw import *
# @lc code=start
from sortedcontainers import SortedList
class MKAverage:

    def __init__(self, m: int, k: int):
        self.k=k
        self.m=m
        self.container=[0]*m
        self.n=m-2*k
        self.idx=0
        self.largek=SortedList()
        self.smallk=SortedList()
        self.middle=SortedList()
        self.s=0


    def addElement(self, num: int) -> None:
        override=self.container[self.idx]
        self.container[self.idx]=num
        self.idx+=1
        if self.idx==self.m:
            self.idx=0
        if override==0:
            self.s+=num
            self.middle.add(num)
            if self.container[self.idx]!=0:
                for _ in range(self.k):
                    last=self.middle.pop()
                    self.s-=last
                    self.largek.add(last)
                    first=self.middle.pop(0)
                    self.s-=first
                    self.smallk.add(first)
        else:
            if num<self.smallk[-1]:
                last=self.smallk.pop()
                self.smallk.add(num)
                self.middle.add(last)
                self.s+=last
            elif num>self.largek[0]:
                first=self.largek.pop(0)
                self.largek.add(num)
                self.middle.add(first)
                self.s+=first
            else:
                self.middle.add(num)
                self.s+=num

            if override<self.middle[0]:
                self.smallk.remove(override)
                first=self.middle.pop(0)
                self.s-=first
                self.smallk.add(first)
            elif override<self.largek[0]:
                self.middle.remove(override)
                self.s-=override
            else:
                self.largek.remove(override)
                last=self.middle.pop()
                self.s-=last
                self.largek.add(last)

    def calculateMKAverage(self) -> int:
        if not self.largek:
            return -1
        return self.s//self.n


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

obj=MKAverage(3,1)
obj.addElement(3716)
obj.addElement(51094)
assert obj.calculateMKAverage()==-1
obj.addElement(56724)
obj.addElement(79619)
assert obj.calculateMKAverage()==56724
obj.addElement(99914)
obj.addElement(277)
assert obj.calculateMKAverage()==79619
obj.addElement(91205)

obj = MKAverage(3, 1); 
obj.addElement(3);        # 当前元素为 [3]
obj.addElement(1);        # 当前元素为 [3,1]
assert obj.calculateMKAverage()==-1; # 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       # 当前元素为 [3,1,10]
assert obj.calculateMKAverage()==3; # 最后 3 个元素为 [3,1,10]
                          # 删除最小以及最大的 1 个元素后，容器为 [3]
                          # [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        # 当前元素为 [3,1,10,5]
obj.addElement(5);        # 当前元素为 [3,1,10,5,5]
obj.addElement(5);        # 当前元素为 [3,1,10,5,5,5]
assert obj.calculateMKAverage()==5; # 最后 3 个元素为 [5,5,5]
                          # 删除最小以及最大的 1 个元素后，容器为 [5]
                          # [5] 的平均值等于 5/1 = 5 ，故返回 5