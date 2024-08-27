#
# @lc app=leetcode.cn id=2064 lang=python3
# @lcpr version=30204
#
# [2064] 分配给商店的最多商品的最小值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        M=len(quantities)
        left=1
        right=max(quantities)
        ret=0
        while left<=right:
            mid=(left+right)>>1
            cnt=n
            for q in quantities:
                cnt-=(q-1)//mid+1
            if cnt>=0:
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret
# @lc code=end
assert Solution().minimizedMaximum(7,[15,10,10])==5
assert Solution().minimizedMaximum(1,[100000])==100000
assert Solution().minimizedMaximum(n = 6, quantities = [11,6])==3


#
# @lcpr case=start
# 6\n[11,6]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[15,10,10]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[100000]\n
# @lcpr case=end

#

