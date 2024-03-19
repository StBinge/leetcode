#
# @lc app=leetcode.cn id=1387 lang=python3
#
# [1387] 将整数按权重排序
#
from sbw import *
# @lc code=start
import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def get_weight(n:int):
            if n==1:
                return 0

            if n%2:
                n=n*3+1
            else:
                n>>=1
            return 1+get_weight(n)
        
        q=[]
        for i in range(lo,lo+k):
            heapq.heappush(q,[-get_weight(i),-i])
        for i in range(lo+k,hi+1):
            heapq.heappushpop(q,[-get_weight(i),-i])
        return -q[0][1]
# @lc code=end
assert Solution().getKth(lo = 7, hi = 11, k = 4)==7
assert Solution().getKth(12,15,2)==13
