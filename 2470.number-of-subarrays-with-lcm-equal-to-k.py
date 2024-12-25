#
# @lc app=leetcode.cn id=2470 lang=python3
# @lcpr version=30204
#
# [2470] 最小公倍数为 K 的子数组数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        _k = k
        factors = [1]
        f = 2
        while f <= k:
            if k % f != 0:
                f += 1
                continue
            ff = 1
            while k % f == 0:
                ff *= f
                k //= f
            factors.append(ff)
        cnt = defaultdict(int)
        N = len(nums)
        dp = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            if _k % nums[i] == 0:
                dp[i] = dp[i + 1] + 1

        ret = 0
        left = 0
        valid = 0
        f_cnt = len(factors)
        for i in range(N):
            if dp[i] == 0:
                left = i + 1
                cnt.clear()
                valid = 0
                continue
            n = nums[i]
            for f in factors:
                if n % f == 0:
                    cnt[f] += 1
                    if cnt[f] == 1:
                        valid += 1
            if valid == f_cnt:
                x = dp[i]
                while valid == f_cnt:
                    ret += x
                    pre = nums[left]
                    for f in factors:
                        if pre % f == 0:
                            cnt[f] -= 1
                            if cnt[f] == 0:
                                valid -= 1
                    left += 1
        return ret


# @lc code=end
assert Solution().subarrayLCM(nums=[3, 6, 2, 7, 1], k=6) == 4
assert Solution().subarrayLCM([3, 10, 8, 7, 20, 2, 13, 15, 14, 12], 6) == 0
assert Solution().subarrayLCM(nums=[1], k=1) == 1
assert Solution().subarrayLCM(nums=[3], k=2) == 0


#
# @lcpr case=start
# [3,6,2,7,1]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3]\n2\n
# @lcpr case=end

#
