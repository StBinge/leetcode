#
# @lc app=leetcode.cn id=1943 lang=python3
# @lcpr version=30204
#
# [1943] 描述绘画结果
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        axis=defaultdict(int)
        for l,r,c in segments:
            axis[l]+=c
            axis[r]-=c
        sorted_axis=sorted([k,v] for k,v in axis.items())
        for i in range(1,len(sorted_axis)):
            sorted_axis[i][1]+=sorted_axis[i-1][1]
        ret=[]
        for x,y in pairwise(sorted_axis):
            if x[1]:
                ret.append([x[0],y[0],x[1]])
        return ret



# @lc code=end
assert Solution().splitPainting( [[1,4,5],[1,4,7],[4,7,1],[4,7,11]])==[[1,4,12],[4,7,12]]
assert Solution().splitPainting([[1,7,9],[6,8,15],[8,10,7]])==[[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
assert Solution().splitPainting( [[1,4,5],[4,7,7],[1,7,9]])==[[1,4,14],[4,7,16]]


#
# @lcpr case=start
# [[1,4,5],[4,7,7],[1,7,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,7,9],[6,8,15],[8,10,7]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]\n
# @lcpr case=end

#

