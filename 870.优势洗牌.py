#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
from typing import List


# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort(reverse=True)
        num2_idx = sorted([(n, i) for i, n in enumerate(nums2)], reverse=True)
        ans = [0] * len(nums1)
        idx = 0
        tai = len(nums1) - 1
        for n, i in num2_idx:
            if nums1[idx] > n:
                ans[i] = nums1[idx]
                idx += 1
            else:
                ans[i] = nums1[tai]

                tai -= 1

        return ans


# @lc code=end
nums1 = [12, 24, 8, 32]
nums2 = [13, 25, 32, 11]
ret = [24, 32, 8, 12]
assert Solution().advantageCount(nums1, nums2) == ret

nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]
ret = [2, 11, 7, 15]
assert Solution().advantageCount(nums1, nums2) == ret

