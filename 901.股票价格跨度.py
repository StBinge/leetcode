#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack=[[-1,float('inf')]]
        self.idx=-1

    def next(self, price: int) -> int:
        self.idx+=1
        while price>=self.stack[-1][1]:
            self.stack.pop()
        self.stack.append([self.idx,price])
        return self.idx-self.stack[-2][0]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
stockSpanner = StockSpanner()
assert stockSpanner.next(28)==1 # 返回 1
assert stockSpanner.next(14)==1 # 返回 1
assert stockSpanner.next(28)==3 # 返回 1

stockSpanner = StockSpanner()
assert stockSpanner.next(100)==1 # 返回 1
assert stockSpanner.next(80)==1  # 返回 1
assert stockSpanner.next(60)==1  # 返回 1
assert stockSpanner.next(70)==2  # 返回 2
assert stockSpanner.next(60)==1  # 返回 1
assert stockSpanner.next(75)==4  # 返回 4 ，因为截至今天的最后 4 个股价 (包括今天的股价 75) 都小于或等于今天的股价。
assert stockSpanner.next(85)==6  # 返回 6