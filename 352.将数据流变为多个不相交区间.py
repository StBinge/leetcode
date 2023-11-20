#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
from typing import List
# @lc code=start
fro
class LinkNode:
    def __init__(self,min:int,max:int,pre:'LinkNode'=None,nxt:'LinkNode'=None) -> None:
        self.min=min
        self.max=max
        self.pre=pre
        self.nxt=nxt
class SummaryRanges:

    def __init__(self):
        self.head=LinkNode(-2,-2)
        self.tail=LinkNode(10**5,10**5)
        self.head.nxt=self.tail
        self.tail.pre=self.head


    def addNum(self, value: int) -> None:
        cur=self.head
        while cur:
            if value+1==cur.min:
                cur.min=value
                if cur.pre.max+1==cur.min:
                    cur.pre.max=cur.max
                    cur.pre.nxt=cur.nxt
                    cur.nxt.pre=cur.pre
                    del cur
                break
            if value==cur.max+1:
                cur.max=value
                if cur.nxt and cur.nxt.min-1==cur.max:
                    old_nxt=cur.nxt
                    cur.max=old_nxt.max
                    cur.nxt=old_nxt.nxt
                    cur.nxt.pre=cur
                    del old_nxt
                    
                break
            if value<cur.min:
                node=LinkNode(value,value)
                cur.pre.nxt=node
                node.nxt=cur
                node.pre=cur.pre
                cur.pre=node
                break

            if value<=cur.max:
                break

            cur=cur.nxt


    def getIntervals(self) -> List[List[int]]:
        ret=[]
        cur=self.head.nxt
        while cur!=self.tail:
            ret.append([cur.min,cur.max])
            cur=cur.nxt
        return ret


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end
obj=SummaryRanges()
obj.addNum(1)
print(obj.getIntervals())
obj.addNum(0)
print(obj.getIntervals())
obj.addNum(3)
print(obj.getIntervals())
obj.addNum(7)
print(obj.getIntervals())
obj.addNum(2)
print(obj.getIntervals())
obj.addNum(6)
print(obj.getIntervals())
