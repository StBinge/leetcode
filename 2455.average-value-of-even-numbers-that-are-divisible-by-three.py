#
# @lc app=leetcode.cn id=2455 lang=python3
# @lcpr version=30204
#
# [2455] 可被三整除的偶数的平均值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=cnt=0
        for n in nums:
            if n%6==0:
                s+=n
                cnt+=1
        return s//cnt if cnt>0 else 0
        
# @lc code=end



#
# @lcpr case=start
# [1,3,6,10,12,15]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,7,10]\n
# @lcpr case=end

#

