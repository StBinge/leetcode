#
# @lc app=leetcode.cn id=2176 lang=python3
# @lcpr version=30204
#
# [2176] 统计数组中相等且可以被整除的数对
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ret=0
        pos_cache=defaultdict(list)
        for i,n in enumerate(nums):
            for pos in pos_cache[n]:
                if i*pos % k==0:
                    ret+=1
            pos_cache[n].append(i)
        return ret
# @lc code=end



#
# @lcpr case=start
# [3,1,2,2,2,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n1\n
# @lcpr case=end

#

