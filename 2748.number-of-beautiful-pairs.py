#
# @lc app=leetcode.cn id=2748 lang=python3
# @lcpr version=30204
#
# [2748] 美丽下标对的数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt=[0]*10
        ret=0
        availables=[
            [],# 0
            [1,2,3,4,5,6,7,8,9],# 1
            [1,3,5,7,9],# 2
            [1,2,4,5,7,8],# 3
            [1,3,5,7,9],# 4
            [1,2,3,4,6,7,8,9],# 5
            [1,5,7],# 6
            [1,2,3,4,5,6,8,9],# 7
            [1,3,5,7,9],# 8
            [1,2,4,5,7,8],# 9
        ]
        for n in nums:
            last=n%10
            ret+=sum(cnt[i] for i in availables[last])
            while n>9:
                n//=10
            cnt[n]+=1
        return ret
# @lc code=end
assert Solution().countBeautifulPairs([64,23,99,83,5,21,76,34,99,63])==25


#
# @lcpr case=start
# [2,5,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [11,21,12]\n
# @lcpr case=end

#

