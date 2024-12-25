#
# @lc app=leetcode.cn id=2570 lang=python3
# @lcpr version=30204
#
# [2570] 合并两个二维数组 - 求和法
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i1=i2=0
        n1,n2=len(nums1),len(nums2)
        ret=[]
        while i1<n1 and i2<n2:
            id1,v1=nums1[i1]
            id2,v2=nums2[i2]
            if id1==id2:
                ret.append([id1,v1+v2])
                i1+=1
                i2+=1
            elif id1<id2:
                ret.append([id1,v1])
                i1+=1
            else:
                ret.append([id2,v2])
                i2+=1

        ret.extend(nums2[i2:])
        ret.extend(nums1[i1:])
        return ret
# @lc code=end
assert Solution().mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]])==[[1,6],[2,3],[3,2],[4,6]]


#
# @lcpr case=start
# [[1,2],[2,3],[4,5]]\n[[1,4],[3,2],[4,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,6],[5,5]]\n[[1,3],[4,3]]\n
# @lcpr case=end

#

