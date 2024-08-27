#
# @lc app=leetcode.cn id=2044 lang=python3
# @lcpr version=30204
#
# [2044] 统计按位或能得到最大值的子集数目
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N=len(nums)
        cache={}
        cache[0]=0
        ret=0
        Mx=0
        for i in range(N):
            n=nums[i]
            for j in range(1<<i):
                cur=n|cache[j]
                if cur>Mx:
                    Mx=cur
                    ret=1
                elif cur==Mx:
                    ret+=1
                cache[(1<<i) | j]=cur
        return ret
# @lc code=end
assert Solution().countMaxOrSubsets([3,2,1,5])==6
assert Solution().countMaxOrSubsets([2,2,2])==7
assert Solution().countMaxOrSubsets([3,1])==2


#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,5]\n
# @lcpr case=end

#

