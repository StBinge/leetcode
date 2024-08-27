#
# @lc app=leetcode.cn id=2104 lang=python3
# @lcpr version=30204
#
# [2104] 子数组范围和
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N=len(nums)
        mx_st=[]
        mi_st=[]
        ret=0
        for i,cur in enumerate(nums):
            while mx_st and cur>=nums[mx_st[-1]]:
                p_mx=mx_st.pop()
                pp_mx=mx_st[-1] if mx_st else -1
                left_cnt=p_mx-pp_mx
                right_cnt=i-p_mx
                ret+=nums[p_mx]*right_cnt*left_cnt
            mx_st.append(i)

            while mi_st and cur<=nums[mi_st[-1]]:
                p_mi=mi_st.pop()
                pp_mi=mi_st[-1] if mi_st else -1
                left_cnt=p_mi-pp_mi
                right_cnt=i-p_mi
                ret-=nums[p_mi]*left_cnt*right_cnt
            mi_st.append(i)

        while mx_st:
            cur_mx=mx_st.pop()
            p_mx=mx_st[-1] if mx_st else -1
            ret+=nums[cur_mx]*(N-cur_mx)*(cur_mx-p_mx)


        while mi_st:
            cur_mi=mi_st.pop()
            p_mi=mi_st[-1] if mi_st else -1
            ret-=nums[cur_mi]*(N-cur_mi)*(cur_mi-p_mi)
        return ret

# @lc code=end
assert Solution().subArrayRanges([4,-2,-3,4,1])==59
assert Solution().subArrayRanges([1,2,3])==4


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,-2,-3,4,1]\n
# @lcpr case=end

#

