#
# @lc app=leetcode.cn id=1357 lang=python3
#
# [1357] 每隔 n 个顾客打折
#
from sbw import *
# @lc code=start
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.cnt=0
        self.prices={prod:price for prod,price in zip(products,prices)}
        self.discount=(100-discount)/100

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt+=1
        money=0
        for p,num in zip(product,amount):
            money+=self.prices[p]*num
        if self.cnt==self.n:
            money*=self.discount
            self.cnt=0
        return money


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
# @lc code=end

