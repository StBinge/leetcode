#
# @lc app=leetcode.cn id=3224 lang=python3
# @lcpr version=30204
#
# [3224] 使差值相等的最少数组改动次数
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt1=[0]*(k+1)
        cnt2=[0]*(k+1)
        ret=N
        for i in range(N//2):
            x,y=nums[i],nums[-1-i]
            if x>y:
                x,y=y,x
            cnt1[y-x]+=1
            cnt2[max(y,k-x)]+=1
        s=0
        for c1,c2 in zip(cnt1,cnt2):
            ret=min(ret,N//2-c1+s)
            s+=c2
        return ret


# @lc code=end
assert Solution().minChanges([18,10,14,18,17,2,11,5],19) == 2
assert Solution().minChanges(nums = [0,1,2,3,3,6,5,4], k = 6) == 2
assert Solution().minChanges(nums=[1, 0, 1, 2, 4, 3], k=4) == 2


#
# @lcpr case=start
# [1,0,1,2,4,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,3,3,6,5,4]\n6\n
# @lcpr case=end

#
