#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#
from sbw import *
# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks={v:i for i,v in enumerate(sorted(set(arr)),1)}
        ret=[0]*len(arr)
        for i in range(len(arr)):
            ret[i]=ranks[arr[i]]
        return ret
# @lc code=end
assert Solution().arrayRankTransform([40,10,20,30])==[4,1,2,3]
assert Solution().arrayRankTransform([1,1,1])==[1,1,1]
