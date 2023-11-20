#
# @lc app=leetcode.cn id=731 lang=python3
#
# [731] 我的日程安排表 II
#

# @lc code=start
import bisect
class MyCalendarTwo:

    def __init__(self):
        self.overlaps=[]
        self.booked=[]



    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlaps:
            if start<e and s<end:
                return False
        
        for s,e in self.booked:
            if start<e and s<end:
                self.overlaps.append([max(start,s),min(end,e)])
        self.booked.append([start,end])
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
# @lc code=end

MyCalendar=MyCalendarTwo()
assert MyCalendar.book(10, 20)# # returns True
assert MyCalendar.book(50, 60)# # returns True
assert MyCalendar.book(10, 40)# # returns True
assert not MyCalendar.book(5, 15)# # returns False
assert MyCalendar.book(5, 10)# # returns True
assert MyCalendar.book(25, 55)# # returns True

MyCalendar =MyCalendarTwo()
args=[[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
rets=[None,True,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,False]
for i in range(1,len(rets)):
    assert MyCalendar.book(*args[i])==rets[i]
    