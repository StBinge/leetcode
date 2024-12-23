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
        self.cnt=[0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i,m in enumerate(banknotesCount):
            self.cnt[i]+=m

    def withdraw(self, amount: int) -> List[int]:
        notes=[20,50,100,200,500]
        ret=[0]*5
        for i in range(4,-1,-1):
            if amount==0:
                break
            if self.cnt[i]==0:
                continue
            if self.cnt[i]*notes[i]<amount:
                ret[i]=self.cnt[i]
                amount-=self.cnt[i]*notes[i]
            else:
                c,amount=divmod(amount,notes[i])
                ret[i]=c
        if amount>0:
            return [-1]
        
        for i,c in enumerate(ret):
            self.cnt[i]-=c
        return ret
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end
test_obj(ATM,["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"],[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]],'[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]')
test_obj(ATM,["ATM","deposit","withdraw"],[[],[[0,0,1,0,1]],[100]],'[null,null,[0,0,1,0,0]]')


#
# @lcpr case=start
# ["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"][[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]\n
# @lcpr case=end

#

