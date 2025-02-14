#
# @lc app=leetcode.cn id=2607 lang=python3
# @lcpr version=30204
#
# [2607] 使子数组元素和相等
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        N = len(arr)
        if k==N:
            return 0
        if k==1 or N % k:
            s = sum(arr)
            avg = s // N
            ret = sum(abs(n-avg) for n in arr)
            if s % N:
                ret=min(ret,sum(abs(n-avg-1) for n in arr))

            return ret

        ret = 0
        pairs = N // k
        for i in range(k):
            s = sum(arr[i::k])
            avg = s // pairs
            r = sum(abs(arr[i] - avg) for i in range(0, N, k))
            if s % pairs:
                r = min(r, sum(abs(arr[j] - avg - 1) for j in range(i, N, k)))
            ret += r
        return ret


# @lc code=end
assert Solution().makeSubKSumEqual([2,10,9],1) == 8
assert Solution().makeSubKSumEqual([4,6],2) == 0
assert Solution().makeSubKSumEqual(arr = [2,5,5,7], k = 3) == 5
assert Solution().makeSubKSumEqual(arr=[1, 4, 1, 3], k=2) == 1


#
# @lcpr case=start
# [1,4,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,5,5,7]\n3\n
# @lcpr case=end

#
