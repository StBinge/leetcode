#
# @lc app=leetcode.cn id=2615 lang=python3
# @lcpr version=30204
#
# [2615] 等值距离和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        N=len(nums)
        cnt=defaultdict(list)
        for i,n in enumerate(nums):
            cnt[n].append(i)
        
        ret=[0]*N
        for indices in cnt.values():
            M=len(indices)
            if M<2:
                continue
            s=sum(indices)
            pre=0
            for i,idx in enumerate(indices):
                ret[idx]=i*idx - pre + s-idx*(M-i)
                pre+=idx
                s-=idx
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,3,1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,5,3]\n
# @lcpr case=end

#

