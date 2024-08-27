#
# @lc app=leetcode.cn id=2090 lang=python3
# @lcpr version=30204
#
# [2090] 半径为 k 的子数组平均值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        ret=[-1]*N
        if N<k*2+1:
            return ret
        cnt=2*k+1
        s=sum(nums[:cnt-1])
        
        for i in range(k,N-k):
            s+=nums[i+k]
            ret[i]=s//cnt
            s-=nums[i-k]
        return ret
# @lc code=end



#
# @lcpr case=start
# [7,4,3,9,1,8,5,2,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [100000]\n0\n
# @lcpr case=end

# @lcpr case=start
# [8]\n100000\n
# @lcpr case=end

#

