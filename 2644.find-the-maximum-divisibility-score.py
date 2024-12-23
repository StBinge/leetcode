#
# @lc app=leetcode.cn id=2644 lang=python3
# @lcpr version=30204
#
# [2644] 找出可整除性得分最大的整数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        dup=sum(x==y for x,y in pairwise(nums))
        divisors.sort()
        ret=divisors[0]
        max_cnt=-1
        for d in divisors:
            if (max_cnt-dup+1)*d>nums[0]:
                break
            cnt=0
            for n in nums:
                if n<d:
                    break
                if n%d==0:
                    cnt+=1
            if cnt>max_cnt:
                max_cnt=cnt
                ret=d
        return ret
# @lc code=end
assert Solution().maxDivScore(nums = [2,9,15,50], divisors = [5,3,7,2])==2


#
# @lcpr case=start
# [2,9,15,50]\n[5,3,7,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,7,9,3,9]\n[5,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [20,14,21,10]\n[10,16,20]\n
# @lcpr case=end

#

