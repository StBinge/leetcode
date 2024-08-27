#
# @lc app=leetcode.cn id=1601 lang=python3
#
# [1601] 最多可达成的换楼请求数目
#
from sbw import *
# @lc code=start
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ret=0
        N=len(requests)
        for mask in range((1<<N)-1,-1,-1):
            if mask.bit_length()<=ret:
                break
            cnt=mask.bit_count()
            if cnt<=ret:
                continue
            delta=[0]*n
            for i,[x,y] in enumerate(requests):
                if mask & (1<<i):
                    delta[x]-=1
                    delta[y]+=1
            if all(x==0 for x in delta):
                ret=cnt
        return ret
# @lc code=end
assert Solution().maximumRequests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]])==4
assert Solution().maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]])==3
assert Solution().maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]])==5
