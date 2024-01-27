#
# @lc app=leetcode.cn id=1172 lang=python3
#
# [1172] 餐盘栈
#

# @lc code=start
from sortedcontainers.sortedset import SortedSet

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack=[]
        self.cap=capacity
        self.top=[]
        self.popped=SortedSet()

    def push(self, val: int) -> None:
        if not self.popped:
            pos=len(self.stack)
            self.stack.append(val)
            if pos%self.cap==0:
                self.top.append(0)
            else:
                self.top[-1]+=1
        else:
            pos=self.popped.pop(0)
            self.stack[pos]=val
            idx=pos//self.cap
            self.top[idx]+=1

    def pop(self) -> int:
        while self.popped and self.stack and self.popped[-1]==len(self.stack)-1:
            self.stack.pop()
            pos=self.popped.pop()
            if pos%self.cap==0:
                self.top.pop()
        if not self.stack:
            return -1
        
        pos=len(self.stack)-1
        val=self.stack.pop()
        if pos % self.cap==0 and self.top:
            self.top.pop()
        elif self.top:
            self.top[-1]-=1
        return val
    
    def popAtStack(self, index: int) -> int:
        if index>=len(self.top):
            return -1
        pos=self.top[index]
        if pos<0:
            return -1
        self.top[index]-=1
        idx=index*self.cap+pos
        self.popped.add(idx)
        return self.stack[idx]





# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# @lc code=end

plates=DinnerPlates(2)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.popAtStack(0)
plates.push(20) 
plates.push(21)
plates.popAtStack(0)
plates.popAtStack(2)
assert plates.pop()==5  
assert plates.pop()==4   
assert plates.pop() ==3
assert plates.pop() ==1
assert plates.pop()==-1 