#
# @lc app=leetcode.cn id=2915 lang=python3
# @lcpr version=30204
#
# [2915] 和为目标值的最长子序列的长度
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f=[float('-inf')]*(target+1)
        f[0]=0
        s=0
        for n in nums:
            s=min(target,s+n)
            for t in range(s,n-1,-1):
                f[t]=max(f[t],f[t-n]+1)
        return f[-1] if f[-1]>float('-inf') else -1

# @lc code=end
assert Solution().lengthOfLongestSubsequence(nums = [1,1,5,4,5], target = 3)==-1
assert Solution().lengthOfLongestSubsequence(nums = [4,1,3,2,1,5], target = 7)==4
assert Solution().lengthOfLongestSubsequence(nums = [1,2,3,4,5], target = 9)==3


#
# @lcpr case=start
# [1,2,3,4,5]\n9\n
# @lcpr case=end

# @lcpr case=start
# [4,1,3,2,1,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5,4,5]\n3\n
# @lcpr case=end

#

