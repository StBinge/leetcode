#
# @lc app=leetcode.cn id=2034 lang=python3
# @lcpr version=30204
#
# [2034] 股票价格波动
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.lasted_time=-1
        self.lasted_price=-1
        self.records={}
        self.prices=SortedList()

    def update(self, timestamp: int, price: int) -> None:
        self.prices.add([price,timestamp])
        self.records[timestamp]=price
        if timestamp>=self.lasted_time:
            self.lasted_price=price
            self.lasted_time=timestamp

    def current(self) -> int:
        return self.lasted_price

    def maximum(self) -> int:
        while True:
            price,ts=self.prices[-1]
            if self.records[ts]!=price:
                self.prices.pop()
            else:
                return price
        

    def minimum(self) -> int:
        while True:
            price,ts=self.prices[0]
            if self.records[ts]!=price:
                self.prices.pop(0)
            else:
                return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end

ops=["StockPrice","update","maximum","current","minimum","maximum","maximum","maximum","minimum","minimum","maximum","update","maximum","minimum","update","maximum","minimum","current","maximum","update","minimum","maximum","update","maximum","maximum","current","update","current","minimum","update","update","minimum","minimum","update","current","update","maximum","update","minimum"]

args=[[],[38,2308],[],[],[],[],[],[],[],[],[],[47,7876],[],[],[58,1866],[],[],[],[],[43,121],[],[],[40,5339],[],[],[],[32,5339],[],[],[43,6414],[49,9369],[],[],[36,3192],[],[48,1006],[],[53,8013],[]]
outputs=eval_list_str('[null,null,2308,2308,2308,2308,2308,2308,2308,2308,2308,null,7876,2308,null,7876,1866,1866,7876,null,121,7876,null,7876,7876,1866,null,1866,121,null,null,1866,1866,null,1866,null,9369,null,1006]')

obj=StockPrice()
for i in range(1,len(ops)):
    if ops[i]=='update':
        obj.update(*args[i])
    elif ops[i]=='current':
        assert obj.current()==outputs[i]
    elif ops[i]=='maximum':
        assert obj.maximum()==outputs[i]
    elif ops[i]=='minimum':
        assert obj.minimum()==outputs[i]
    else:
        raise "Wrong op"


#
# @lcpr case=start
# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"][[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]\n
# @lcpr case=end

#

