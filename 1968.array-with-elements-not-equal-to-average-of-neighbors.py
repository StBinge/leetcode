#
# @lc app=leetcode.cn id=1968 lang=python3
# @lcpr version=30204
#
# [1968] 构造元素不等于两相邻元素平均值的数组
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        N=len(nums)

        ret=[]

        for i in range(N//2):
            ret.append(nums[i])
            ret.append(nums[-1-i])
        if N&1:
            ret.append(nums[N//2])

        return ret
            
# @lc code=end
def test(ar:list):
    N=len(ar)
    for i in range(N-2):
        assert ar[i]+ar[i+2]!=ar[i]*2

test(Solution().rearrangeArray([6,2,0,9,7]))
test(Solution().rearrangeArray([1,2,3,4,5]))

#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [6,2,0,9,7]\n
# @lcpr case=end

#

