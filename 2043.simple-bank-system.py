#
# @lc app=leetcode.cn id=2043 lang=python3
# @lcpr version=30204
#
# [2043] 简易银行系统
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Bank:

    def __init__(self, balance: List[int]):
        self.accounts=balance
        self.n=len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 0<account1<=self.n and 0<account2<=self.n and self.accounts[account1-1]>=money:
            self.accounts[account1-1]-=money
            self.accounts[account2-1]+=money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<self.n:
            self.accounts[account]+=money
            return True
        return False


    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<self.n and self.accounts[account]>=money:
            self.accounts[account]-=money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end
bank = Bank([10, 100, 20, 50, 30])#
assert bank.withdraw(3, 10)
assert bank.transfer(5, 1, 20)
assert bank.deposit(5, 20)
assert bank.transfer(3, 4, 15)==False
assert bank.withdraw(10, 50)==False#


#
# @lcpr case=start
# ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"][[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]\n
# @lcpr case=end

#

