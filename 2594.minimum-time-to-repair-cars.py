#
# @lc app=leetcode.cn id=2594 lang=python3
# @lcpr version=30204
#
# [2594] 修车的最少时间
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left=1
        right=min(ranks)*cars*cars

        cnts=Counter(ranks)
        # def check(x):
        #     cnt=0
        #     for r in ranks:
        #         cnt+=int(math.sqrt(x/r))
        #     return cnt>=cars
        
        ret=0
        while left<=right:
            mid=(left+right)>>1
            if sum(c*math.isqrt(mid//r) for r,c in cnts.items())>=cars:
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret
# @lc code=end
assert Solution().repairCars(ranks = [5,1,8], cars = 6)==16
assert Solution().repairCars(ranks = [4,2,3,1], cars = 10)==16


#
# @lcpr case=start
# [4,2,3,1]\n10\n
# @lcpr case=end

# @lcpr case=start
# [5,1,8]\n6\n
# @lcpr case=end

#

