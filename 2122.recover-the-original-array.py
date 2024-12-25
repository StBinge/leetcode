#
# @lc app=leetcode.cn id=2122 lang=python3
# @lcpr version=30204
#
# [2122] 还原原数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        N=len(nums)
        ret=[0]*(N//2)
        for i in range(1,N//2+1):
            used=[False]*N
            used[i]=True
            d=nums[i]-nums[0]
            if d<1 or d&1:
                continue
            idx=i+1
            ret[0]=nums[0]+d//2
            cnt=1
            for j in range(1,N):
                if used[j]:
                    continue
                ret[cnt]=nums[j]+d//2
                cnt+=1
                hi=nums[j]+d
                while idx<N and nums[idx]!=hi:
                    idx+=1
                if idx==N:
                    break
                used[idx]=True
                idx+=1
            else:
                return ret

# @lc code=end
assert Solution().recoverArray([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9])==[2,3,7,8,8,9,9,10]
assert Solution().recoverArray([1,1,3,3])==[2,2]
assert Solution().recoverArray([2,10,6,4,8,12])==[3,7,11]


#
# @lcpr case=start
# [2,10,6,4,8,12]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,435]\n
# @lcpr case=end

#

