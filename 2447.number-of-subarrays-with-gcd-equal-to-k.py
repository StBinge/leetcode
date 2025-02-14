#
# @lc app=leetcode.cn id=2447 lang=python3
# @lcpr version=30204
#
# [2447] 最大公因数等于 K 的子数组数目
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        a=[]
        i0=-1
        ret=0
        for i,x in enumerate(nums):
            if x%k:
                a=[]
                i0=i
                continue
            a.append([x,i])
            j=0
            for p in a:
                p[0]=math.gcd(p[0],x)
                if p[0]==a[j][0]:
                    a[j][1]=p[1]
                else:
                    a[j]=p
            if a[0][0]==k:
                ret+=a[0][1]-i0
        return ret
                
# @lc code=end
assert Solution().subarrayGCD([9,3,3,1,2,6,3],3)==7
assert Solution().subarrayGCD([9,3,1,2,6,3],3)==4
assert Solution().subarrayGCD([5],1)==0
assert Solution().subarrayGCD([4],7)==0

#
# @lcpr case=start
# [9,3,1,2,6,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4]\n7\n
# @lcpr case=end

#

