#
# @lc app=leetcode.cn id=2780 lang=python3
# @lcpr version=30204
#
# [2780] 合法分割的最小下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        domain=-1
        cnt=0
        for n in nums:
            if domain==n:
                cnt+=1
            else:
                if cnt==0:
                    domain=n
                    cnt=1
                else:
                    cnt-=1
        cnt=nums.count(domain)
        N=len(nums)
        if N&1 and cnt==(N+1)//2:
            return -1
        
        pre=0
        for i,n in enumerate(nums):
            if n==domain:
                pre+=1
                cnt-=1
            if pre*2>i+1 and cnt*2>N-i-1:
                return i
        return -1
# @lc code=end



#
# @lcpr case=start
# [1,2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,1,1,1,7,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,7,2,2]\n
# @lcpr case=end

#

