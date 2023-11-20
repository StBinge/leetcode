#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#
from typing import List
# @lc code=start
import heapq
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        ret=0
        pre=float('-inf')
        for start,end in pairs:
            if pre>=start:
                continue
            ret+=1
            pre=end
        return ret
        # pairs=sorted([[pairs[i][1]-pairs[i][0],pairs[i][1]] for i in range(len(pairs))],key=lambda x:x[1])
        # stack=[]
        # edge=-1
        # for length, end in pairs:
        #     if not stack:
        #         stack.append(length)
        #         edge=end
        #         continue
        #     if length+edge<end:
        #         heapq.heappush(stack,length)
        #         edge=end
        #         continue
        #     while stack and stack[0]>length:
        #         stack.pop()
        #     heapq.heappush(stack,length)
        #     edge=end
        # return len(stack)

# @lc code=end
pairs = [[1,2], [2,3], [3,4]]
assert Solution().findLongestChain(pairs)==2
pairs = [[1,2],[7,8],[4,5]]
assert Solution().findLongestChain(pairs)==3
