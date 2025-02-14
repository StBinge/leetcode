#
# @lc app=leetcode.cn id=2261 lang=python3
# @lcpr version=30204
#
# [2261] 含最多 K 个可整除元素的子数组
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ret = 0
        N = len(nums)
        vis = set()
        mod1 = 10**9 + 7
        mod2 = 10**9 + 11
        for i in range(N):
            cnt = 0
            h1=h2=0
            for j in range(i, N):
                cnt += int(nums[j] % p == 0)
                if cnt > k:
                    break
                h1 = (h1 * 211 + nums[j]) % mod1
                h2 = (h2 * 203 + nums[j]) % mod2
                if (h1,h2) in vis:
                    continue
                ret += 1
                vis.add((h1,h2))
        return ret


# @lc code=end
assert Solution().countDistinct([15,36,58,72,23,71,73,48,43,17,67,90,76,96,4,68,19,33,55,51,37,23,98,46,65,88,5,4,78,10,100,1,18,8,96,98,81,22,12,3,55,38,69,96,32,38,16,11,12,51,93,91,72,16,43,48,69,38,10,91,99,57,67,19,13,12,80,27,96,11,86,33,51,33,12,37,42,33,47,17,6,4,54,32,41,81,24,88,65,1,71,100,5,96,10,87,89,44,86,86,40,60,97,27,91,14,63,94,35,41,38,46,33,91,49,86,65,26,56,3,6,30,54,78,23,34,4,56,20,52,92,74,39,22,27,51,92,41,38,71,9,40,16,53,28,86,95,94,33,59,100,39,34,79,84,92,66,69,28,32,83,5,89,14,8,49,52,78,11,30,45,94,92,93,44,26,76,72,62,17,3,3,50],54,67) == 16739
assert Solution().countDistinct(nums=[1, 2, 3, 4], k=4, p=1) == 10
assert Solution().countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2) == 11


#
# @lcpr case=start
# [2,3,3,2,2]\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n4\n1\n
# @lcpr case=end

#
