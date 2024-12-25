#
# @lc app=leetcode.cn id=2200 lang=python3
# @lcpr version=30204
#
# [2200] 找出数组中的所有 K 近邻下标
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret=[]
        left=0
        N=len(nums)
        for i,n in enumerate(nums):
            if n!=key:
                continue
            left=max(left,i-k)
            right=min(i+k,N-1)
            for j in range(left,right+1):
                ret.append(j)
            left=right+1
        return ret
# @lc code=end



#
# @lcpr case=start
# [3,4,9,1,3,9,5]\n9\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n2\n2\n
# @lcpr case=end

#

