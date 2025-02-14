#
# @lc app=leetcode.cn id=2597 lang=python3
# @lcpr version=30204
#
# [2597] 美丽子集的数目
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups=defaultdict(Counter)
        for n in nums:
            groups[n%k][n]+=1
        
        ret=1
        for cnt in groups.values():
            sorted_x=sorted(cnt.keys())
            N=len(sorted_x)
            f0=1
            f1=1<<cnt[sorted_x[0]]
            for i in range(1,N):
                if sorted_x[i]!=sorted_x[i-1]+k:
                    f=f1<<cnt[sorted_x[i]]
                else:
                    f=f0*((1<<cnt[sorted_x[i]])-1)+f1
                f0,f1=f1,f
            ret*=f1
        return ret-1
                
# @lc code=end
assert Solution().beautifulSubsets([1,2,3,3],1)==8
assert Solution().beautifulSubsets([4,2,5,9,10,3],1)==23
assert Solution().beautifulSubsets([1],1)==1
assert Solution().beautifulSubsets([2,4,6],2)==4


#
# @lcpr case=start
# [2,4,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

