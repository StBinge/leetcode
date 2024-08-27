#
# @lc app=leetcode.cn id=1671 lang=python3
#
# [1671] 得到山形数组的最少删除次数
#
from sbw import *
# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N=len(nums)
        
        def get_dp(array):
            f=[]
            seq=[]
            for n in array:
                idx=bisect.bisect_left(seq,n)
                if idx==len(seq):
                    f.append(idx+1)
                    seq.append(n)
                else:
                    seq[idx]=n
                    f.append(idx+1)
            return f
        
        prefix=get_dp(nums)
        sufix=get_dp(nums[::-1])[::-1]
        ret=0
        for i in range(1,N-1):
            if sufix[i]>1 and prefix[i]>1:
                ret=max(prefix[i]+sufix[i],ret)
        return N-ret+1
# @lc code=end
assert Solution().minimumMountainRemovals([100,92,89,77,74,66,64,66,64])==6
assert Solution().minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1])==2
assert Solution().minimumMountainRemovals([1,3,1])==0
assert Solution().minimumMountainRemovals([2,1,1,5,6,2,3,1])==3
