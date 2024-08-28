#
# @lc app=leetcode.cn id=2025 lang=python3
# @lcpr version=30204
#
# [2025] 分割数组的最多方案数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        N=len(nums)
        presums=list(accumulate(nums,initial=0))
        tot=presums[-1]
        counter=Counter(presums)
        counter[0]-=1
        counter[tot]-=1
        ret=0
        if tot&1==0:
            ret=counter[tot>>1]
        pre_cnt=defaultdict(int)
        pre_s=0
        for n in nums:
            if n!=k:                
                dif=k-n
                _tot=tot-n+k
                if _tot&1==0:
                    half=_tot//2
                    ret=max(counter[half-dif]+pre_cnt[half],ret)
            pre_s+=n
            pre_cnt[pre_s]+=1
            counter[pre_s]-=1
        return ret

# @lc code=end
assert Solution().waysToPartition([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30827,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0)==33


#
# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

# @lcpr case=start
# [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]\n-33\n
# @lcpr case=end

#

