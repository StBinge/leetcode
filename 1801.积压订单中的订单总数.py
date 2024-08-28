#
# @lc app=leetcode.cn id=1801 lang=python3
#
# [1801] 积压订单中的订单总数
#
from sbw import *
# @lc code=start
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # price,amount
        buy_heap=[]
        sell_heap=[]
        for p,m,t in orders:
            # buy need sell<buy
            if t==0:
                while m and sell_heap and sell_heap[0][0]<=p:
                    if m<sell_heap[0][1]:
                        sell_heap[0][1]-=m
                        m=0
                    else:
                        m-=heapq.heappop(sell_heap)[1]
                if m:
                    heapq.heappush(buy_heap,[-p,m])
            # sell, need buy>sell
            else:
                while m and buy_heap and -buy_heap[0][0]>=p:
                    if m<buy_heap[0][1]:
                        buy_heap[0][1]-=m
                        m=0
                    else:
                        m-=heapq.heappop(buy_heap)[1]
                if m:
                    heapq.heappush(sell_heap,[p,m])
        return (sum(x[1] for x in buy_heap)+sum(x[1] for x in sell_heap))%(10**9+7)
# @lc code=end

assert Solution().getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]])==999999984
assert Solution().getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]])==6