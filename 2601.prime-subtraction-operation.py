#
# @lc app=leetcode.cn id=2601 lang=python3
# @lcpr version=30204
#
# [2601] 质数减法运算
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        mx = max(nums)
        is_prime = [True] * max(2, mx)
        is_prime[0] = is_prime[1] = False
        for i in range(2, mx):
            if is_prime[i] == False:
                continue
            for j in range(i + i, mx, i):
                is_prime[j] = False
        primes = [i for i, f in enumerate(is_prime) if f]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            idx = bisect_right(primes, nums[i] - nums[i + 1])
            if idx == len(primes) or primes[idx] >= nums[i]:
                return False
            nums[i] -= primes[idx]
        return True


# @lc code=end
assert Solution().primeSubOperation([6,8,11,12])
assert Solution().primeSubOperation([4, 9, 6, 10])
assert Solution().primeSubOperation([5, 8, 3]) == False


#
# @lcpr case=start
# [4,9,6,10]\n
# @lcpr case=end

# @lcpr case=start
# [6,8,11,12]\n
# @lcpr case=end

# @lcpr case=start
# [5,8,3]\n
# @lcpr case=end

#
