#
# @lc app=leetcode.cn id=2598 lang=python3
# @lcpr version=30204
#
# [2598] 执行操作后的最大 MEX
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt=Counter([n%value for n in nums])
        ret=0
        while cnt[ret%value]>0:
            cnt[ret%value]-=1
            ret+=1
        return ret
        
# @lc code=end
assert Solution().findSmallestInteger([3,0,3,2,4,2,1,1,0,4],5) == 10


#
# @lcpr case=start
# [1,-10,7,13,6,8]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,-10,7,13,6,8]\n7\n
# @lcpr case=end

#

