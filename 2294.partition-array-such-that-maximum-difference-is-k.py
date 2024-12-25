#
# @lc app=leetcode.cn id=2294 lang=python3
# @lcpr version=30204
#
# [2294] 划分数组使最大差为 K
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mi=nums[0]
        ret=0
        for i in range(1,len(nums)):
            if mi+k>=nums[i]:
                continue
            ret+=1
            mi=nums[i]
        return ret+1
# @lc code=end



#
# @lcpr case=start
# [3,6,1,2,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,4,5]\n0\n
# @lcpr case=end

#

