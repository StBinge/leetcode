#
# @lc app=leetcode.cn id=2588 lang=python3
# @lcpr version=30204
#
# [2588] 统计美丽子数组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ret=0
        cnt=defaultdict(int)
        cnt[0]=1
        mask=0

        for n in nums:
            mask^=n
            ret+=cnt[mask]
            cnt[mask]+=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [4,3,1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,10,4]\n
# @lcpr case=end

#

