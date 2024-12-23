#
# @lc app=leetcode.cn id=2865 lang=python3
# @lcpr version=30204
#
# [2865] 美丽塔 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        N=len(heights)
        left_sum=[0]*N
        left_sum[0]=heights[0]
        # height,left_most_idx
        pre_heights=[[heights[0],0]]
        for i in range(1,N):
            if heights[i]<heights[i-1]:
                idx=0
                while pre_heights and pre_heights[-1][0]>heights[i]:
                    idx=pre_heights.pop()[1]
                s=heights[i]*(i-idx+1) + (left_sum[idx-1] if idx>0 else 0)
                left_sum[i]=s
                pre_heights.append([heights[i],idx])
            else:
                if heights[i]>heights[i-1]:
                    pre_heights.append([heights[i],i])
                left_sum[i]=left_sum[i-1]+heights[i]
        
        right_sum=[0]*N
        right_sum[-1]=heights[-1]
        pre_heights=[[heights[-1],N-1]]
        ret=left_sum[-1]
        for i in range(N-2,-1,-1):
            if heights[i]<heights[i+1]:
                idx=N-1
                while pre_heights and pre_heights[-1][0]>heights[i]:
                    idx=pre_heights.pop()[1]
                s=heights[i]*(idx-i+1) + (right_sum[idx+1] if idx+1<N else 0)
                right_sum[i]=s
                pre_heights.append([heights[i],idx])
            else:
                if heights[i]>heights[i+1]:
                    pre_heights.append([heights[i],i])
                right_sum[i]=right_sum[i+1]+heights[i]
            ret=max(left_sum[i]+right_sum[i]-heights[i],ret)
        return ret


                
# @lc code=end
assert Solution().maximumSumOfHeights([1,3,5,4,6,1,6,3,1,2])==23
assert Solution().maximumSumOfHeights([5,3,4,1,1])==13
assert Solution().maximumSumOfHeights([3,2,5,5,2,3])==18
assert Solution().maximumSumOfHeights([999999999,1000000000])==1999999999
assert Solution().maximumSumOfHeights([6,5,3,9,2,7])==22


#
# @lcpr case=start
# [5,3,4,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,3,9,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,5,5,2,3]\n
# @lcpr case=end

#

