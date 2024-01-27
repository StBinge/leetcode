#
# @lc app=leetcode.cn id=1105 lang=python3
#
# [1105] 填充书架
#
from sbw import *
# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        L=len(books)
        f=[float('inf')]*(L+1)
        f[0]=0
        for i in range(L):
            # thinck,height=books[i]
            cur_width=0
            max_height=0
            j=i
            while j>=0:
                cur_width+=books[j][0]
                if cur_width>shelfWidth:
                    break
                max_height=max(max_height,books[j][1])
                f[i+1]=min(f[i+1],f[j]+max_height)
                j-=1
        return f[-1]
# @lc code=end
assert Solution().minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6)==4
assert Solution().minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4)==6

