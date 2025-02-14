#
# @lc app=leetcode.cn id=3354 lang=python3
# @lcpr version=30204
#
# [3354] 使数组元素等于零
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s=sum(nums)
        if s==0:
            return len(nums)*2
        pre=0
        ret=0
        for n in nums:
            if n:
                pre+=n
                s-=n
                continue
            if pre>s+1:
                 break
            dif=abs(pre-s)
            if dif==1:
                ret+=1
            elif dif==0:
                ret+=2
        return ret
# @lc code=end
assert Solution().countValidSelections([1,0,2,0,3])==2


#
# @lcpr case=start
# [1,0,2,0,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,0,4,1,0]\n
# @lcpr case=end

#

