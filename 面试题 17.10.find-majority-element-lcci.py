#
# @lc app=leetcode.cn id=面试题 17.10 lang=python3
# @lcpr version=30204
#
# [面试题 17.10] 主要元素
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=1
        cur=nums[0]
        for n in nums[1:]:
            if n==cur:
                cnt+=1
            else:
                cnt-=1
                if cnt==0:
                    cur=n
                    cnt=1
        return cur if nums.count(cur)*2 >len(nums) else -1
# @lc code=end



#
# @lcpr case=start
# [1,2,5,9,5,9,5,5,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

