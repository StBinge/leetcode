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
        if k == N:
            return 0
        if k == 1 or math.gcd(N,k)==1:
            arr.sort()
            mid = arr[N // 2]
            return sum(abs(n - mid) for n in arr)

        ret = 0
        k=math.gcd(N,k)
        for i in range(k):
            sub=sorted(arr[i::k])
            mid=sub[len(sub)//2]

            ret+=sum(abs(n-mid) for n in sub)
        return ret


# @lc code=end
assert Solution().makeSubKSumEqual([6,2,8,5,7,10],4) == 10
assert Solution().makeSubKSumEqual([8, 2, 5, 9, 8, 10], 2) == 11
assert Solution().makeSubKSumEqual([2, 10, 9], 1) == 8
assert Solution().makeSubKSumEqual([4, 6], 2) == 0
assert Solution().makeSubKSumEqual(arr=[2, 5, 5, 7], k=3) == 5
assert Solution().makeSubKSumEqual(arr=[1, 4, 1, 3], k=2) == 1


#
# @lcpr case=start
# [1,4,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,5,5,7]\n3\n
# @lcpr case=end

#
