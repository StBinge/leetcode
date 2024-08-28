#
# @lc app=leetcode.cn id=2006 lang=python3
# @lcpr version=30204
#
# [2006] 差的绝对值为 K 的数对数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt=defaultdict(int)
        ret=0
        for n in nums:
            ret+=cnt[n+k]+cnt[n-k]
            cnt[n]+=1
        return ret
# @lc code=end
assert Solution().countKDifference(nums = [1,3], k = 3)==0
assert Solution().countKDifference(nums = [1,3], k = 3)==0
assert Solution().countKDifference(nums = [1,2,2,1], k = 1)==4


#
# @lcpr case=start
# [1,2,2,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,5,4]\n2\n
# @lcpr case=end

#

