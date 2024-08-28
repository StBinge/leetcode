#
# @lc app=leetcode.cn id=1711 lang=python3
#
# [1711] 大餐计数
#
from sbw import *


# @lc code=start
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = defaultdict(int)
        Max=max(deliciousness)*2+1
        ret=0
        for x in deliciousness:
            s=1
            while s<Max:
                ret+=counter[s-x]
                s<<=1
            counter[x]+=1
            ret%=10**9+7
        return ret



# @lc code=end
assert Solution().countPairs([1, 1, 1, 3, 3, 3, 7]) == 15
assert Solution().countPairs([1, 3, 5, 7, 9]) == 4
