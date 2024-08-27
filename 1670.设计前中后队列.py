#
# @lc app=leetcode.cn id=1670 lang=python3
#
# [1670] 设计前中后队列
#
from sbw import *
# @lc code=start
class FrontMiddleBackQueue:

    def __init__(self):
        self.front=deque()
        self.back=deque()


    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        if len(self.front)>len(self.back)+1:
            self.back.appendleft(self.front.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.front)==len(self.back)+1:
            self.back.appendleft(self.front.pop())
        
        self.front.append(val)


    def pushBack(self, val: int) -> None:
        self.back.append(val)
        if len(self.front)<len(self.back):
            self.front.append(self.back.popleft())

    def popFront(self) -> int:
        if not self.front:
            return -1
        ret=self.front.popleft()
        if len(self.front)<len(self.back):
            self.front.append(self.back.popleft())
        return ret
    
    def popMiddle(self) -> int:
        if not self.front:
            return -1
        ret=self.front.pop()
        if len(self.front)<len(self.back):
            self.front.append(self.back.popleft())
        return ret


    def popBack(self) -> int:
        if not self.front:
            return -1
        ret=-1
        if self.back:
            ret=self.back.pop()
            if len(self.front)>len(self.back)+1:
                self.back.appendleft(self.front.pop())
            return ret
        return self.front.pop()




# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end
q = FrontMiddleBackQueue()#
q.pushFront(1)#   // [1]
q.pushBack(2)#    // [1, 2]
q.pushMiddle(3)#  // [1, 3, 2]
q.pushMiddle(4)#  // [1, 4, 3, 2]
assert q.popFront()==1#     // 返回 1 -> [4, 3, 2]
assert q.popMiddle()==3#    // 返回 3 -> [4, 2]
assert q.popMiddle()==4#    // 返回 4 -> [2]
assert q.popBack()==2#      // 返回 2 -> []
assert q.popFront()==-1#     // 返回 -1 -> [] （队列为空）
