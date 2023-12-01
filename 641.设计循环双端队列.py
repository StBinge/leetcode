#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[0]*(k+1)
        self.N=k+1
        self.front=0
        self.rear=0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front=(self.front-1)%self.N
        self.queue[self.front]=value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear]=value
        self.rear=(self.rear+1)%self.N
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.N

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear=(self.rear-1)%self.N
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear-1)%self.N]

    def isEmpty(self) -> bool:
        return self.front==self.rear

    def isFull(self) -> bool:
        return self.front==(self.rear+1)%self.N


# Your MyCircularDeque object will be instantiated and called as such:
# @lc code=end
obj = MyCircularDeque(3)
assert obj.insertLast(1)
assert obj.insertLast(2)
assert obj.insertFront(3)
assert obj.insertFront(4) ==False

assert obj.getRear()==2
assert obj.isFull()
assert obj.deleteLast()
assert obj.insertFront(4)
assert obj.getFront()==4
