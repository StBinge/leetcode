#
# @lc app=leetcode.cn id=1218 lang=python3
#
# [1218] 最长定差子序列
#
from sbw import *
# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen=defaultdict(int)
        for n in arr:
            seen[n]=seen[n-difference]+1
        return max(seen.values())
# @lc code=end
assert Solution().longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8],0)==2
assert Solution().longestSubsequence([1,2,3,2,3],1)==3
assert Solution().longestSubsequence([7,-2,8,10,6,18,9,-8,-5,18,13,-6,-17,-1,-6,-9,9,9],1)==3
assert Solution().longestSubsequence(arr = [1,3,5,7], difference = 1)==1
assert Solution().longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2)==4
assert Solution().longestSubsequence(arr = [1,2,3,4], difference = 1)==4
