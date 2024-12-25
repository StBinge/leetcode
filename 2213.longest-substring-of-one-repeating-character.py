#
# @lc app=leetcode.cn id=2213 lang=python3
# @lcpr version=30204
#
# [2213] 由单个字符重复的最长子字符串
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        N=len(s)
        edges=[[0,0] for _ in range(N)]
        left=''
        left_idx=-1
        for i,ch in enumerate(s):
            if left!=ch:
                left=ch
                left_idx=i
            edges[i][0]=left_idx
        right=''
        right_idx=N
        for i in range(N-1,-1,-1):
            if right!=s[i]:
                right_idx=i
                right=s[i]
            edges[i][1]=right_idx
        
        len_cnt=defaultdict(int)
        for l,r in edges:
            
            
# @lc code=end



#
# @lcpr case=start
# "babacc"\n"bcb"\n[1,3,3]\n
# @lcpr case=end

# @lcpr case=start
# "abyzz"\n"aa"\n[2,1]\n
# @lcpr case=end

#

