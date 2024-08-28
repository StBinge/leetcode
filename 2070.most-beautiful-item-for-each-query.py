#
# @lc app=leetcode.cn id=2070 lang=python3
# @lcpr version=30204
#
# [2070] 每一个查询的最大美丽值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        N=len(queries)
        qindices=list(range(N))
        qindices.sort(key=queries.__getitem__)
        ret=[0]*N
   
        mx=0
        idx=0
        M=len(items)
        for q in qindices:
            p=queries[q]
            while idx<M and items[idx][0]<=p:
                mx=max(mx,items[idx][1])
                idx+=1
            ret[q]=mx
        return ret
        
# @lc code=end
assert Solution().maximumBeauty([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]],[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584])==[962,962,962,962,746,962,962,962,946,962,962,919,746,746,962,962,962,919,962]
assert Solution().maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6])==[2,4,5,5,6,6]


#
# @lcpr case=start
# [[1,2],[3,2],[2,4],[5,6],[3,5]]\n[1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,3],[1,4]]\n[1]\n
# @lcpr case=end

# @lcpr case=start
# [[10,1000]]\n[5]\n
# @lcpr case=end

#

