#
# @lc app=leetcode.cn id=2537 lang=python3
# @lcpr version=30204
#
# [2537] 统计好子数组的数目
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # x = math.ceil(math.sqrt(2 * k + 0.25) + 0.5)
        ret =left= 0
        cnt=defaultdict(int)
        cur=0
        for x in nums:
            cur+=cnt[x]
            cnt[x]+=1
            while cur>=k:
                y=nums[left]
                cnt[y]-=1
                cur-=cnt[y]
                left+=1
            ret+=left
        return ret


# @lc code=end
assert Solution().countGood(nums = [3,1,4,3,2,2,4], k = 2) == 4
assert Solution().countGood(nums=[1, 1, 1, 1, 1], k=10) == 1


#
# @lcpr case=start
# [1,1,1,1,1]\n10\n
# @lcpr case=end

# @lcpr case=start
# [3,1,4,3,2,2,4]\n2\n
# @lcpr case=end

#
