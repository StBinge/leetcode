#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.slots=['']*n
        self.ptr=0
        self.n=n        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.slots[idKey-1]=value
        ret=[]
        for i in range(self.ptr,self.n):
            if self.slots[i]:
                ret.append(self.slots[i])
            else:
                self.ptr=i
                break
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

