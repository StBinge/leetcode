#
# @lc app=leetcode.cn id=3162 lang=python3
# @lcpr version=30204
#
# [3162] 优质数对的总数 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt1=Counter(nums1)
        cnt2=Counter([n*k for n in nums2])
        mx=max(nums1)
        ret=0
        for k,v in cnt2.items():
            v1=sum(cnt1[k1] for k1 in range(k,mx+1,k))
            ret+=v*v1
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,3,4]\n[1,3,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,12]\n[2,4]\n3\n
# @lcpr case=end

#

