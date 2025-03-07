#
# @lc app=leetcode.cn id=2772 lang=python3
# @lcpr version=30204
#
# [2772] 使数组中的所有元素都等于零
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        N=len(nums)
        dif=[0]*(N+1)
        cur=0
        for idx,n in enumerate(nums):
            cur+=dif[idx]
            d=n+cur
            if d<0:
                return False
            if d>0:
                if idx+k>N:
                    return False
                cur-=d
                dif[idx+k]=d
        return True

# @lc code=end
assert Solution().checkArray([0,72],2)==False
assert Solution().checkArray(nums = [1,3,1,1], k = 2)==False
assert Solution().checkArray(nums = [2,2,3,1,1,0], k = 3)


#
# @lcpr case=start
# [2,2,3,1,1,0]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1,1]\n2\n
# @lcpr case=end

#

