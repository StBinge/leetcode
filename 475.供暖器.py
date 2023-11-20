#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
from typing import List
# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        idx=0
        radius=0
        N=len(heaters)
        neg=-10**11
        pos=10**11
        for h in houses:
            while idx<N and heaters[idx]<h:
                idx+=1
            left=heaters[idx-1] if idx-1>=0 else neg
            right=heaters[idx] if idx<N else pos
            radius=max(radius,min(h-left,right-h))
        return radius

# @lc code=end
houses = [474833169,264817709,998097157,817129560]
heaters = [197493099,404280278,893351816,505795335]
assert Solution().findRadius(houses,heaters)==104745341

houses = [1,2,3]
heaters = [2]
assert Solution().findRadius(houses,heaters)==1

houses = [1,2,3,4]
heaters = [1,4]
assert Solution().findRadius(houses,heaters)==1

houses = [1,5]
heaters = [2]
assert Solution().findRadius(houses,heaters)==3

