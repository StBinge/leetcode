#
# @lc app=leetcode.cn id=2932 lang=python3
# @lcpr version=30204
#
# [2932] 找出强数对的最大异或值 I
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ret=mask=0
        hi=nums[-1].bit_length()-1
        for i in range(hi,-1,-1):
            mask|=1<<i
            new_ret=ret|(1<<i)
            cache={}
            for y in nums:
                mask_y=y&mask
                if new_ret ^ mask_y in cache and cache[new_ret^mask_y]*2>=y:
                    ret=new_ret
                    break
                cache[mask_y]=y
        return ret
# @lc code=end
assert Solution().maximumStrongPairXor(list(range(1,6)))==7


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [10,100]\n
# @lcpr case=end

# @lcpr case=start
# [5,6,25,30]\n
# @lcpr case=end

#

