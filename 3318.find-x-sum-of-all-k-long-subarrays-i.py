#
# @lc app=leetcode.cn id=3318 lang=python3
# @lcpr version=30204
#
# [3318] 计算子数组的 x-sum I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if k==x:
            ret=[]
            s=sum(nums[:k-1])
            for i in range(k-1,len(nums)):
                s+=nums[i]
                ret.append(s)
                s-=nums[i-k+1]
            return ret
        cnt=Counter(nums[:k-1])
        ret=[]
        for i in range(k-1,len(nums)):
            cnt[nums[i]]+=1
            s=0
            for n,v in sorted([-v,-n] for n,v in cnt.items())[:x]:
                s+=n*v
            ret.append(s)
            cnt[nums[i-k+1]]-=1
        return ret
# @lc code=end
assert Solution().findXSum([4,1,2,3,3],4,3)==[9,9]
assert Solution().findXSum([50,50,50,50,50,50],6,1)==[300]
assert Solution().findXSum([1,2,3,4,5,6],6,1)==[6]
assert Solution().findXSum([3,8,7,8,7,5],2,2)==[11,15,15,15,12]
assert Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2)==[6,10,12]


#
# @lcpr case=start
# [1,1,2,2,3,4,2,3]\n6\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,8,7,8,7,5]\n2\n2\n
# @lcpr case=end

#

