#
# @lc app=leetcode.cn id=2080 lang=python3
# @lcpr version=30204
#
# [2080] 区间内查询数字的频率
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.positions=defaultdict(list)
        for i,n in enumerate(arr):
            self.positions[n].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        pos=self.positions[value]
        start=bisect_left(pos,left)
        end=bisect_right(pos,right,lo=start)
        return end-start


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end
query=RangeFreqQuery([2,2,1,2,2])
assert query.query(2,4,1)==1
assert query.query(1,3,1)==1
assert query.query(0,2,1)==1
rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])#
assert rangeFreqQuery.query(1, 2, 4)==1# // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
assert rangeFreqQuery.query(0, 11, 33)==2# // 返回 2 。33 在整个子数组中出现 2 次。


#
# @lcpr case=start
# ["RangeFreqQuery", "query", "query"][[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]\n
# @lcpr case=end

#

