#
# @lc app=leetcode.cn id=1686 lang=python3
#
# [1686] 石子游戏 VI
#
from sbw import *


# @lc code=start
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        buckets=[[] for _ in range(201)]
        for a,b in zip(aliceValues,bobValues):
            buckets[a+b].append([a,b])

        alice_sum=0
        bob_sum=0
        idx=0
        for bucket in buckets[::-1]:
            for v in bucket:
                if idx%2:
                    bob_sum+=v[1]
                else:
                    alice_sum+=v[0]
                idx+=1
        # values.sort(reverse=True)
        # alice_sum=sum(v[1] for v in values[::2])
        # bob_sum=sum(v[2] for v in values[1::2])
        if alice_sum>bob_sum:
            return 1
        elif alice_sum==bob_sum:
            return 0
        return -1


# @lc code=end
assert Solution().stoneGameVI(aliceValues = [2,4,3], bobValues = [1,6,7]) == -1
assert Solution().stoneGameVI(aliceValues=[1, 2], bobValues=[3, 1]) == 0
assert Solution().stoneGameVI(aliceValues=[1, 3], bobValues=[2, 1]) == 1
