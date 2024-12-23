#
# @lc app=leetcode.cn id=2364 lang=python3
# @lcpr version=30204
#
# [2364] 统计坏数对的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        for i,n in enumerate(nums):
            cnt[n-i]+=1
        N=len(nums)
        tot=N*(N-1)//2
        return tot-sum(v*(v-1)//2 for v in cnt.values())

# @lc code=end
assert Solution().countBadPairs([1,2,3,4,5])==0
assert Solution().countBadPairs([4,1,3,3])==5


#
# @lcpr case=start
# [4,1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#

