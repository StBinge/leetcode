#
# @lc app=leetcode.cn id=2333 lang=python3
# @lcpr version=30204
#
# [2333] 最小差值平方和
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k=k1+k2
        difs=[abs(x-y) for x,y in zip(nums1,nums2)]
        if sum(difs)<=k:
            return 0
        cnt=Counter(difs)
        sorted_keys=sorted(cnt.keys(),reverse=True)
        N=len(sorted_keys)
        pre_cnt=0
        sorted_keys.append(0)
        for i in range(N):
            x,y=sorted_keys[i],sorted_keys[i+1]
            pre_cnt+=cnt[x]
            if (x-y)*pre_cnt<=k:
                k-=(x-y)*pre_cnt
                continue
            rm,extra=divmod(k,pre_cnt)
            return (x-rm)**2*(pre_cnt-extra)+(x-rm-1)**2*extra+sum(sorted_keys[j]**2*cnt[sorted_keys[j]] for j in range(i+1,N))


# @lc code=end
assert Solution().minSumSquareDiff([7,11,4,19,11,5,6,1,8],[4,7,6,16,12,9,10,2,10],3,6)==27
assert Solution().minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1)==43
assert Solution().minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0)==579


#
# @lcpr case=start
# [1,2,3,4]\n[2,10,20,19]\n0\n0\n
# @lcpr case=end

# @lcpr case=start
# [1,4,10,12]\n[5,8,6,9]\n1\n1\n
# @lcpr case=end

#

