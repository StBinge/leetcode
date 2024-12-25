#
# @lc app=leetcode.cn id=2461 lang=python3
# @lcpr version=30204
#
# [2461] 长度为 K 子数组中的最大和
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        mx_s = 0
        cnt = Counter(nums[: k - 1])
        s = sum(nums[: k - 1])
        single = sum(v == 1 for v in cnt.values())
        for i in range(k - 1, len(nums)):
            x = nums[i]
            cnt[x] += 1
            s += x
            if cnt[x] == 1:
                single += 1
            elif cnt[x]==2:
                single -= 1
            if single == k:
                mx_s = max(s, mx_s)
            y = nums[i - k + 1]
            cnt[y] -= 1
            if cnt[y] == 1:
                single += 1
            elif cnt[y]==0:
                single -= 1
            s -= y
        return mx_s


# @lc code=end
assert Solution().maximumSubarraySum([1,1,1,7,8,9],3) == 24
assert Solution().maximumSubarraySum(nums=[4, 4, 4], k=3) == 0
assert Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3) == 15


#
# @lcpr case=start
# [1,5,4,2,9,9,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4]\n3\n
# @lcpr case=end

#
