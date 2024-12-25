#
# @lc app=leetcode.cn id=LCR 059 lang=python3
# @lcpr version=30204
#
# [LCR 059] 数据流中的第 K 大元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val>self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
obj=KthLargest(3, [4, 5, 8, 2])
ops=["KthLargest", "add", "add", "add", "add", "add"]
args=[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
ret='[null, 4, 5, 5, 8, 8]'
test_obj(obj,ops,args,ret)


#
# @lcpr case=start
# ["KthLargest", "add", "add", "add", "add", "add"][[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]\n
# @lcpr case=end

#

