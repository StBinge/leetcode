#
# @lc app=leetcode.cn id=638 lang=python3
#
# [638] 大礼包
#
from typing import List
# @lc code=start


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        L = len(price)
        valid_sp = []
        for bundle in special:
            total = 0

            for i in range(L):
                total += price[i]*bundle[i]
                if bundle[i]>needs[i]:
                    break
            else:
                if total > bundle[-1]:
                    valid_sp.append(bundle)

        memo = {}

        def buy(needs: list):
            nonlocal L
            hash = tuple(needs)
            if hash in memo:
                return memo[hash]
            spent = 0
            for i in range(L):
                spent += price[i]*needs[i]

            for sp in valid_sp:
                needs_copy = needs.copy()
                # can_buy=True
                for i in range(L):
                    needs_copy[i] -= sp[i]
                    if needs_copy[i] < 0:
                        # can_buy=False
                        break
                else:
                    spent = min(sp[-1]+buy(needs_copy), spent)
            memo[hash] = spent
            return spent
        r= buy(needs)
        return r


# @lc code=end
price = [2, 5]
special = [[3, 0, 5], [1, 2, 10]]
needs = [3, 2]
assert Solution().shoppingOffers(price, special, needs) == 14

price = [2, 3, 4]
special = [[1, 1, 0, 4], [2, 2, 1, 9]]
needs = [1, 2, 1]
assert Solution().shoppingOffers(price, special, needs) == 11
