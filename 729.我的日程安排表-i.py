#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#
from typing import List
# @lc code=start

class MyCalendar:

    def __init__(self):
        self.tree=set()
        self.lazy=set()
    
    def __query(self,start,end,l,r,idx):
        if end<l or start>r:
            return False
        if idx in self.lazy:
            return True
        if start<=l and r<=end:
            return idx in self.tree
        
        mid=(l+r)//2
        return self.__query(start,end,l,mid,idx*2) or self.__query(start,end,mid+1,r,idx*2+1)

    def __update(self,start,end,l,r,index):
        if end<l or r<start:
            return
        if start<=l and r<=end:
            self.tree.add(index)
            self.lazy.add(index)
            return

        mid=(l+r)//2
        self.__update(start,end,l,mid,index*2)
        self.__update(start,end,mid+1,r,index*2+1)
        self.tree.add(index)
        if index*2 in self.lazy and index*2+1 in self.lazy:
            self.lazy.add(index)
    # def __update(self, start: int, end: int, l: int, r: int, idx: int) -> None:
    #     if r < start or end < l:
    #         return
    #     if start <= l and r <= end:
    #         self.tree.add(idx)
    #         self.lazy.add(idx)
    #     else:
    #         mid = (l + r) // 2
    #         self.__update(start, end, l, mid, 2 * idx)
    #         self.__update(start, end, mid + 1, r, 2 * idx + 1)
    #         self.tree.add(idx)
    #         if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
    #             self.lazy.add(idx)


    def book(self, start: int, end: int) -> bool:
        if self.__query(start,end-1,0,10**9,1):
            return False
        self.__update(start,end-1,0,10**9,1)
        return True
        
    
                               




# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

myCalendar = MyCalendar()#
assert myCalendar.book(10, 20)# // return True
assert not myCalendar.book(15, 25)# // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
assert myCalendar.book(20, 30)# // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。