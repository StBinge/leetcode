#
# @lc app=leetcode.cn id=2438 lang=python3
# @lcpr version=30204
#
# [2438] 二的幂数组中查询范围内的乘积
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers=[]
        i=0
        while n>=(1<<i):
            if n & (1<<i):
                powers.append(i)
            i+=1
        pre_sum=[0]
        for p in powers:
            pre_sum.append(pre_sum[-1]+p)
        ret=[]
        for l,r in queries:
            exp=pre_sum[r+1]-pre_sum[l]
            ret.append(pow(2,exp,10**9+7))
        return ret
# @lc code=end
assert Solution().productQueries(n = 2, queries = [[0,0]])==[2]
assert Solution().productQueries(n = 15, queries = [[0,1],[2,2],[0,3]])==[2,4,64]


#
# @lcpr case=start
# 15\n[[0,1],[2,2],[0,3]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0]]\n
# @lcpr case=end

#

