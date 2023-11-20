#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
from typing import List
# @lc code=start
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        f=[envelopes[0][1]]
        for i in range(1,len(envelopes)):
            h=envelopes[i][1]
            if h>f[-1]:
                f.append(envelopes[i][1])
            if h<f[-1]:
                left,right=0,len(f)-1
                while left<right:
                    mid=(left+right)//2
                    mid_h=f[mid]
                    if mid_h<h:
                        left=mid+1
                    elif mid_h>=h:
                        right=mid            
                f[left]=h
        # for i in range(1, len(envelopes)):
        #     if (num := envelopes[i][1]) > f[-1]:
        #         f.append(num)
        #     else:
        #         index = bisect.bisect_left(f, num)
        #         f[index] = num


        return len(f)
        

# @lc code=end
# [1, 4, 25, 28, 30, 37, 40]
assert Solution().maxEnvelopes([[36,36],[1,4],[27,27],[13,6],[38,14],[14,25],[25,38],[5,7],[50,25],[27,49],[40,50],[39,46],[34,8],[9,5],[2,30],[19,35],[7,40],[42,14],[6,1],[30,15],[17,35],[18,28],[35,36],[24,44],[41,35],[48,20],[7,37]])==9
assert Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])==3
assert Solution().maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])==3
assert Solution().maxEnvelopes([[1,1],[1,1],[1,1]])==1