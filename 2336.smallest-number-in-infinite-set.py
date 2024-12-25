#
# @lc app=leetcode.cn id=2336 lang=python3
# @lcpr version=30204
#
# [2336] 无限集中的最小数字
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.pushback=[]
        self.edge=1
        self.popped=[False]*1001

    def popSmallest(self) -> int:
        if self.pushback:
            ret= heapq.heappop(self.pushback)
            self.popped[ret]=True
            return ret
        self.popped[self.edge]=True
        self.edge+=1
        return self.edge-1
    
    def addBack(self, num: int) -> None:
        if self.popped[num]==False:
            return
        if num==self.edge-1:
            self.edge-=1
        elif num<self.edge:
            heapq.heappush(self.pushback,num)
        self.popped[num]=False


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
obj=SmallestInfiniteSet()
ops=["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
args=[[], [2], [], [], [], [1], [], [], []]
answers=eval_list_str('[null, null, 1, 2, 3, null, 1, 4, 5]')
test_obj(obj,ops,args,answers)

