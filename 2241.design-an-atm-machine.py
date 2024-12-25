#
# @lc app=leetcode.cn id=2241 lang=python3
# @lcpr version=30204
#
# [2241] 设计一个 ATM 机器
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class ATM:

    def __init__(self):
        self.vals=[20,50,100,200,500]
        self.cnt=[0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,c in enumerate(banknotesCount):
            self.cnt[i]+=c

    def withdraw(self, amount: int) -> List[int]:
        outs=[0]*5
        for i in range(4,-1,-1):
            if self.cnt[i] and self.vals[i]<=amount:
                c=amount//self.vals[i]
                c=min(c,self.cnt[i])
                outs[i]=c
                amount-=c*self.vals[i]
        if amount!=0:
            return [-1]
        for i,c in enumerate(outs):
            self.cnt[i]-=c
        return outs


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end


#
# @lcpr case=start
# ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"][[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]\n
# @lcpr case=end

#

