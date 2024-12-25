#
# @lc app=leetcode.cn id=2799 lang=python3
# @lcpr version=30204
#
# [2799] 统计完全子数组的数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        K=len(set(nums))
        cnt=defaultdict(int)
        N=len(nums)
        left=0
        ret=0
        for right in range(N):
            cnt[nums[right]]+=1
            if cnt[nums[right]]==1:
                K-=1
            if K==0:
                while left<right and cnt[nums[left]]>1:
                    cnt[nums[left]]-=1
                    left+=1
                ret+=left+1
        return ret



# @lc code=end
assert Solution().countCompleteSubarrays([1898,370,822,1659,1360,128,370,360,261,1898]) == 4
assert Solution().countCompleteSubarrays([1, 3, 1, 2, 2]) == 4
assert (
    Solution().countCompleteSubarrays([459, 459, 962, 1579, 1435, 756, 1872, 1597]) == 2
)


#
# @lcpr case=start
# [1,3,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5]\n
# @lcpr case=end

#
