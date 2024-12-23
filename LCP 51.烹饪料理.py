#
# @lc app=leetcode.cn id=LCP 51 lang=python3
# @lcpr version=30204
#
# [LCP 51] 烹饪料理
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        if sum(y for _,y in attribute)<limit:
             return -1
        NC=len(cookbooks)
        NM=len(materials)
        ret=-1
        for i in range(1,1<<NC):
            eat=de=0
            valid=True
            mat=[0]*NM
            for j in range(NC):
                if (i>>j)&1==0:
                    continue
                d,e=attribute[j]
                de+=d
                eat+=e
                for k,m in enumerate(cookbooks[j]):
                        mat[k]+=m
                        if mat[k]>materials[k]:
                            valid=False
                            break
                if not valid:
                     break
            if valid and eat>=limit:
                ret=max(ret,de)
        return ret
# @lc code=end
assert Solution().perfectMenu([17,9,18,1,16],[[13,20,10,0,13],[20,14,17,16,18],[1,11,9,12,2],[14,5,0,1,7],[2,3,3,17,12]],[[9,20],[1,8],[13,8],[15,13],[20,14]],57)==-1
assert Solution().perfectMenu( [10,10,10,10,10],[[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]], [[5,5],[6,6],[10,10]],limit = 1)==11
assert Solution().perfectMenu(materials = [3,2,4,1,2],cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]],attribute = [[3,2],[2,4],[7,6]],limit = 5)==7


#
# @lcpr case=start
# [3,2,4,1\n[[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1\n[[3,2],[2,4],[7\n5`>\n
# @lcpr case=end

# @lcpr case=start
# [10,10,10,10\n[[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10\n[[5,5],[6,6],[10\n1`>\n
# @lcpr case=end

#

