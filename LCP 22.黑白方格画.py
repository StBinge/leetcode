#
# @lc app=leetcode.cn id=LCP 22 lang=python3
# @lcpr version=30204
#
# [LCP 22] 黑白方格画
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        k=n*n-k
        if k==0:
            return 1
        i=1
        ret=0
        while i*i<k:
            if k%i==0:
                j=k//i
                ret+=math.comb(n,i)*math.comb(n,j)*2
            i+=1
        if i*i==k:
            ret+=math.comb(n,i)**2
        return ret
# @lc code=end
assert Solution().paintingPlan(2,2)==4
assert Solution().paintingPlan(1,0)==1
assert Solution().paintingPlan(2,4)==1
assert Solution().paintingPlan(2,1)==0


#
# @lcpr case=start
# 2\n2`>\n
# @lcpr case=end

# @lcpr case=start
# 2\n1`>\n
# @lcpr case=end

# @lcpr case=start
# 2\n4`>\n
# @lcpr case=end

#

