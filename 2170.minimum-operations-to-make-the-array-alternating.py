#
# @lc app=leetcode.cn id=2170 lang=python3
# @lcpr version=30204
#
# [2170] 使数组变成交替数组的最少操作数
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter_odd=Counter(nums[1::2])
        counter_even=Counter(nums[0::2])
        def get_mx(cnt:dict):
            k1=k2=-1
            c1=c2=0
            for k,v in cnt.items():
                if v>c1:
                    c1,c2=v,c1
                    k1,k2=k,k1
                elif v>c2:
                    c2=v
                    k2=k
            return k1,k2,c1,c2
        
        ok1,ok2,oc1,oc2=get_mx(counter_odd)
        ek1,ek2,ec1,ec2=get_mx(counter_even)
        if ok1!=ek1:
            return len(nums)-oc1-ec1
        
        return len(nums)-max(oc1+ec2,oc2+ec1)
# @lc code=end



#
# @lcpr case=start
# [3,1,3,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,2,2]\n
# @lcpr case=end

#

