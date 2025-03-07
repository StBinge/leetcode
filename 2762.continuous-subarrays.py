#
# @lc app=leetcode.cn id=2762 lang=python3
# @lcpr version=30204
#
# [2762] 不间断子数组
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ret=0
        left=0
        cnt=defaultdict(int)
        for i,n in enumerate(nums):
            cnt[n]+=1
            while max(cnt)-min(cnt)>2:
                y=nums[left]
                cnt[y]-=1
                if cnt[y]==0:
                    del cnt[y]
                left+=1
            ret+=i-left+1
        return ret


# @lc code=end
assert Solution().continuousSubarrays([65,66,67,66,66,65,64,65,65,64])==43
assert Solution().continuousSubarrays([1,2,3])==6
assert Solution().continuousSubarrays([5,4,2,4])==8


#
# @lcpr case=start
# [5,4,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

