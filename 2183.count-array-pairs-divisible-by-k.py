#
# @lc app=leetcode.cn id=2183 lang=python3
# @lcpr version=30204
#
# [2183] 统计可以被 K 整除的下标对数目
#

from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        factors=[]
        i=1
        while i*i<k:
            if k%i==0:
                factors.append(i)
                factors.append(k//i)
            i+=1
        if i*i==k:
            factors.append(i)

        ret = 0
        all = 0
        for i, n in enumerate(nums):
            g = math.gcd(n, k)
            if g == k:
                ret += i
                all += 1
                continue
            ret += all
            if g == 1:
                continue
            r = k//g
            ret += cnt[r]
            for f in factors:
                if n%f==0:
                    cnt[f]+=1
            
        return ret


# @lc code=end
assert Solution().countPairs([8,10,2,5,9,6,3,8,2],6) == 18
assert Solution().countPairs([1, 2, 3, 4], 5) == 0
assert Solution().countPairs([1, 2, 3, 4, 5], 2) == 7


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n5\n
# @lcpr case=end

#
