#
# @lc app=leetcode.cn id=2032 lang=python3
# @lcpr version=30204
#
# [2032] 至少在两个数组中出现的值
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        cnt=[0]*1001
        for n in nums1:
            cnt[n]|=1
        for n in nums2:
            cnt[n]|=0x10
        for n in nums3:
            cnt[n]|=0x100
        ret=[]
        for i,mask in enumerate(cnt):
            if mask & (mask-1):
                ret.append(i)
        return ret
# @lc code=end



#
# @lcpr case=start
# [1,1,3,2]\n[2,3]\n[3]\n
# @lcpr case=end

# @lcpr case=start
# [3,1]\n[2,3]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n[4,3,3]\n[5]\n
# @lcpr case=end

#

