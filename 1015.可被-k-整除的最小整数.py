#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#

# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0:
            return -1
        r=1%k
        s=set()
        while r>0:
            r=((r)*10+1)%k
            if r in s:
                return -1
            s.add(r)
        return len(s)+1
# @lc code=end
assert Solution().smallestRepunitDivByK(81)==81
assert Solution().smallestRepunitDivByK(1)==1
assert Solution().smallestRepunitDivByK(2)==-1
assert Solution().smallestRepunitDivByK(3)==3
