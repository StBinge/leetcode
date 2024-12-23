#
# @lc app=leetcode.cn id=2770 lang=python3
# @lcpr version=30204
#
# [2770] 达到末尾下标所需的最大跳跃次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        N=len(nums)
        f=[float('-inf')]*N
        f[0]=0
        for i in range(N):
            for j in range(i+1,N):
                if abs(nums[j]-nums[i])<=target:
                    f[j]=max(f[j],f[i]+1)
        return f[-1] if f[-1]>0 else -1
        

# @lc code=end
assert Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 0)==-1
assert Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 3)==5
assert Solution().maximumJumps(nums = [1,3,6,4,1,2], target = 2)==3


#
# @lcpr case=start
# [1,3,6,4,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,6,4,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,6,4,1,2]\n0\n
# @lcpr case=end

#

