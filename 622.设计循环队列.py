#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):

        self.array=[-1]*(k+1)
        self.front=self.rear=0
        self.cap=k+1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.array[self.rear]=value
        self.rear=(self.rear+1)%self.cap
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.cap
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.front]

    def Rear(self) -> int:        
        if self.isEmpty():
            return -1
        return self.array[(self.rear-1)%self.cap]

    def isEmpty(self) -> bool:
        return self.rear==self.front

    def isFull(self) -> bool:
        return (self.rear+1)%self.cap==self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
obj = MyCircularQueue(3)
assert  obj.enQueue(1)
assert obj.enQueue(2)
assert obj.enQueue(3)
assert obj.enQueue(4)==False
assert obj.Front()==1
assert obj.Rear()==3
assert obj.isFull()
assert obj.deQueue()
assert obj.enQueue(4)
assert obj.Rear()==4
assert obj.Front()==2
