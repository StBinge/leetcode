#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#
from sbw import *
# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.size=maxSize

    def push(self, x: int) -> None:
        if len(self.stack)<self.size:
            self.stack.append([0,x])
    def pop(self) -> int:
        if not self.stack:
            return -1
        inc,val=self.stack.pop()
        if self.stack:
            self.stack[-1][0]+=inc
        return val+inc

    def increment(self, k: int, val: int) -> None:
        idx=min(len(self.stack),k)-1
        if idx>=0:
            self.stack[idx][0]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
ops=["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
args=[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
ret=eval_list_str('[null,null,null,2,null,null,null,null,null,103,202,201,-1]')
obj=CustomStack(*args[0])
for op,arg,ans in zip(ops[1:],args[1:],ret[1:]):
    assert ans==CustomStack.__dict__[op](obj,*arg)


