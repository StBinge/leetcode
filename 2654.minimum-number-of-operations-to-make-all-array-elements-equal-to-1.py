#
# @lc app=leetcode.cn id=2654 lang=python3
# @lcpr version=30204
#
# [2654] 使数组所有元素变成 1 的最少操作次数
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt1=nums.count(1)
        if cnt1:
            return len(nums)-cnt1
        if math.gcd(*nums)>1:
            return -1
        N=len(nums)
        ret=N
        a=[]
        for i,x in enumerate(nums):
            a.append([x,i])
            j=0
            for p in a:
                p[0]=math.gcd(p[0],x)
                if p[0]!=a[j][0]:
                    j+=1
                    a[j]=p
                else:
                    a[j][1]=p[1]
            del a[j+1:]
            if a[0][0]==1:
                ret=min(ret,i-a[0][1])
        return N-1+ret
# @lc code=end
assert Solution().minOperations([2,10,6,14])==-1
assert Solution().minOperations([2,6,3,4])==4


#
# @lcpr case=start
# [2,6,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,10,6,14]\n
# @lcpr case=end

#

