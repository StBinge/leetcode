#
# @lc app=leetcode.cn id=2958 lang=python3
# @lcpr version=30204
#
# [2958] 最多 K 个重复元素的最长子数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ret=0
        left=0
        freq=defaultdict(int)
        for right,n in enumerate(nums):
            freq[n]+=1
            if freq[n]>k:
                ret=max(ret,right-left)
                while nums[left]!=n:
                    freq[nums[left]]-=1
                    left+=1
                left+=1
                freq[n]-=1
        return max(ret,len(nums)-left)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1,2,3,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5,5,5,5]\n4\n
# @lcpr case=end

#

