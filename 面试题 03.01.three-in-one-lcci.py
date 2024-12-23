#
# @lc app=leetcode.cn id=面试题 03.01 lang=python3
# @lcpr version=30204
#
# [面试题 03.01] 三合一
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack=[None]*(3*stackSize)
        self.indices=[0,stackSize,2*stackSize]
        self.size=stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.indices[stackNum]==self.size*(stackNum+1):
            return
        self.stack[self.indices[stackNum]]=value
        self.indices[stackNum]+=1

    def pop(self, stackNum: int) -> int:
        if self.indices[stackNum]>stackNum*self.size:
            ret=self.stack[self.indices[stackNum]-1]
            self.indices[stackNum]-=1
            return ret
        return -1

    def peek(self, stackNum: int) -> int:
        if self.indices[stackNum]>stackNum*self.size:
            return self.stack[self.indices[stackNum]-1]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.indices[stackNum]==stackNum*self.size


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
# @lc code=end
obj=TripleInOne(18)
ops=["TripleInOne", "peek", "pop", "isEmpty", "push", "pop", "push", "push", "pop", "push", "push", "isEmpty", "pop", "peek", "push", "peek", "isEmpty", "peek", "pop", "push", "isEmpty", "pop", "peek", "peek", "pop", "peek", "isEmpty", "pop", "push", "isEmpty", "peek", "push", "peek", "isEmpty", "isEmpty", "isEmpty", "isEmpty", "peek", "push", "push", "peek", "isEmpty", "peek", "isEmpty", "push", "push", "push", "peek", "peek", "pop", "push", "push", "isEmpty", "peek", "pop", "push", "peek", "peek", "pop", "isEmpty", "pop", "peek", "peek", "push", "push"]
args=[[18], [1], [2], [1], [2, 40], [2], [0, 44], [1, 40], [0], [1, 54], [0, 42], [0], [1], [1], [0, 56], [2], [0], [2], [2], [1, 15], [1], [1], [0], [2], [0], [0], [1], [0], [0, 32], [0], [0], [0, 30], [2], [1], [1], [0], [0], [0], [0, 56], [1, 40], [2], [0], [0], [0], [2, 11], [0, 16], [0, 3], [2], [0], [2], [0, 39], [0, 63], [1], [2], [0], [2, 36], [1], [0], [2], [1], [0], [1], [2], [0, 8], [0, 38]]
ret='[null,-1,-1,true,null,40,null,null,44,null,null,false,54,40,null,-1,false,-1,-1,null,false,15,56,-1,56,42,false,42,null,false,32,null,-1,false,false,false,false,30,null,null,-1,false,56,false,null,null,null,11,3,11,null,null,false,-1,63,null,40,39,36,false,39,40,-1,null,null]'
test_obj(obj,ops,args,ret)

obj=TripleInOne(1)
ops=["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
args=[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
ret='[null, null, null, 1, -1, -1, true]'
test_obj(obj,ops,args,ret)


#
# @lcpr case=start
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"][[1], [0, 1], [0, 2], [0], [0], [0], [0]]\n
# @lcpr case=end

# @lcpr case=start
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"][[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]\n
# @lcpr case=end

#

