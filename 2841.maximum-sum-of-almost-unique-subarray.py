#
# @lc app=leetcode.cn id=2841 lang=python3
# @lcpr version=30204
#
# [2841] 几乎唯一子数组的最大和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt=Counter(nums[:k-1])
        s=sum(nums[:k-1])
        ret=0
        for i in range(k-1,len(nums)):
            n=nums[i]
            s+=n
            cnt[n]+=1
            if len(cnt)>=m:
                ret=max(ret,s)
            pre=nums[i-k+1]
            if cnt[pre]==1:
                del cnt[pre]
            else:
                cnt[pre]-=1
            s-=pre
        return ret
# @lc code=end
assert Solution().maxSum(nums = [1], m = 1, k = 1)==1
assert Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3)==23
assert Solution().maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)==18


#
# @lcpr case=start
# [2,6,7,3,1,7]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5,9,9,2,4,5,4]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1]\n3\n3\n
# @lcpr case=end

#

