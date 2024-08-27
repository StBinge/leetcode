#
# @lc app=leetcode.cn id=2102 lang=python3
# @lcpr version=30204
#
# [2102] 序列顺序查询
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList
class SORTracker:

    def __init__(self):
        self.larges=[]
        self.smalls=[]

    def add(self, name: str, score: int) -> None:
        s,n=heapq.heappushpop(self.larges,[score,name])
        heapq.heappush(self.smalls,[-s,n])# 名字也需要反向排序, python做不到


    def get(self) -> str:
        s,n=heapq.heappop(self.smalls)
        heapq.heappush(self.larges,[-s,n])
        return n


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()
# @lc code=end
obj=SORTracker()
ops=["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
args=[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
answers='[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]'
test_obj(obj,ops,args,answers)

#
# @lcpr case=start
# ["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"][[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [],[]]\n
# @lcpr case=end

#

