#
# @lc app=leetcode.cn id=1656 lang=python3
# @lcpr version=30204
#
# [1656] 设计有序流
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.slots=[None]*n
        self.ptr=0
        self.n=n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.slots[idKey-1]=value
        ret=[]
        while self.ptr<self.n and self.slots[self.ptr]:
            ret.append(self.slots[self.ptr])
            self.ptr+=1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end
test_obj(OrderedStream,["OrderedStream", "insert", "insert", "insert", "insert", "insert"],[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]],'[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]')


