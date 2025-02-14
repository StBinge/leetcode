#
# @lc app=leetcode.cn id=2962 lang=python3
# @lcpr version=30204
#
# [2962] 统计最大元素出现至少 K 次的子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        cnt = 0
        left = 0
        ret = 0
        for n in nums:
            if n == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ret+=left
        return ret


# @lc code=end
assert Solution().countSubarrays(nums=[1, 4, 2, 1], k=3) == 0
assert Solution().countSubarrays(nums=[1, 3, 2, 3, 3], k=2) == 6


#
# @lcpr case=start
# [1,3,2,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,1]\n3\n
# @lcpr case=end

#
