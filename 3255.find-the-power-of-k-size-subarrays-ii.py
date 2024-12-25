#
# @lc app=leetcode.cn id=3255 lang=python3
# @lcpr version=30204
#
# [3255] 长度为 K 的子数组的能量值 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        ret=[]
        cnt=0
        pre=-1
        for n in nums[:k-1]:
            if pre+1==n:
                cnt+=1
            else:
                cnt=1
            pre=n
        for n in nums[k-1:]:
            if pre+1==n:
                cnt+=1
                if cnt>=k:
                    ret.append(n)
                else:
                    ret.append(-1)
            else:
                ret.append(-1)
                cnt=1
            pre=n
        return ret
# @lc code=end
assert Solution().resultsArray([52,12,13,14],3)==[-1,14]
assert Solution().resultsArray(nums = [3,2,3,2,3,2], k = 2)==[-1,3,-1,3,-1]
assert Solution().resultsArray(nums = [2,2,2,2,2], k = 4)==[-1,-1]
assert Solution().resultsArray(nums = [1,2,3,4,3,2,5], k = 3)==[3,4,-1,-1,-1]


#
# @lcpr case=start
# [1,2,3,4,3,2,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,2,3,2]\n2\n
# @lcpr case=end

#

