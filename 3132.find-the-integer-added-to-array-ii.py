#
# @lc app=leetcode.cn id=3132 lang=python3
# @lcpr version=30204
#
# [3132] 找出与数组相加的整数 II
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(2,-1,-1):
            v=nums2[0]-nums1[i]
            j=0
            for x in nums1[i:]:
                if x+v==nums2[j]:
                    j+=1
                    if j==len(nums2):
                        return v
        


# @lc code=end
assert Solution().minimumAddedInteger([4,6,3,1,4,2,10,9,5],[5,10,3,2,6,1,9])==0
assert Solution().minimumAddedInteger(nums1 = [4,20,16,12,8], nums2 = [14,18,10])==-2
assert Solution().minimumAddedInteger(nums1 = [3,5,5,3], nums2 = [7,7])==2


#
# @lcpr case=start
# [4,20,16,12,8]\n[14,18,10]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,5,3]\n[7,7]\n
# @lcpr case=end

#

