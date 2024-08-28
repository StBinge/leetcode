#
# @lc app=leetcode.cn id=1889 lang=python3
#
# [1889] 装包裹的最小浪费空间
#
from sbw import *


# @lc code=start
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        presums=list(accumulate(packages,initial=0))

        ret=float('inf')
        Mod=10**9+7
        N=len(packages)
        for bbs in boxes:
            bbs.sort()
            if bbs[-1]<packages[-1]:
                continue
            space=0
            pid=0
            for b_size in bbs:
                if b_size<packages[pid]:
                    continue
                nxt_pid=bisect_right(packages,b_size,lo=pid)-1
                cnt=nxt_pid-pid+1
                space+=cnt*b_size-(presums[nxt_pid+1]-presums[pid])
                pid=nxt_pid+1
                if pid==N:
                    break
            ret=min(ret,space)
        return ret%Mod if ret<float('inf') else -1


# @lc code=end

assert Solution().minWastedSpace(packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]) == 9
assert (
    Solution().minWastedSpace(packages=[2, 3, 5], boxes=[[1, 4], [2, 3], [3, 4]]) == -1
)
assert Solution().minWastedSpace(packages=[2, 3, 5], boxes=[[4, 8], [2, 8]]) == 6
