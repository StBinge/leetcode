#
# @lc app=leetcode.cn id=2406 lang=python3
# @lcpr version=30204
#
# [2406] 将区间分为最少组数
#

from sbw import *
from sortedcontainers import SortedList
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        diff=defaultdict(int)
        for s,e in intervals:
            diff[s]+=1
            diff[e+1]-=1
        ret=s=0
        for x in sorted(diff.keys()):
            s+=diff[x]
            ret=max(ret,s)
        return ret
# @lc code=end
assert Solution().minGroups([[229966,812955],[308778,948377],[893612,952735],[395781,574123],[478514,875165],[766513,953839],[460683,491583],[133951,212694],[376149,838265],[541380,686845],[461394,568742],[804546,904032],[422466,467909],[557048,758709],[680460,899053],[110928,267321],[470258,650065],[534607,921875],[292993,994721],[645020,692560],[898840,947977],[33584,330630],[903142,970252],[17375,626775],[804313,972796],[582079,757160],[785002,987823],[599263,997719],[486500,527956],[566481,813653],[211239,863969],[808577,883125],[21880,516436],[264747,412144],[327175,772333],[984807,988224],[758172,916673],[23583,406006],[954674,956043],[379202,544291],[688869,785368],[841735,983869],[99836,916620],[332504,740696],[740840,793924],[896607,920924],[868540,922727],[125849,550941],[433284,685766]])==19
assert Solution().minGroups([[1,3],[5,6],[8,10],[11,13]])==1
assert Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]])==3


#
# @lcpr case=start
# [[5,10],[6,8],[1,5],[2,3],[1,10]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[5,6],[8,10],[11,13]]\n
# @lcpr case=end

#

