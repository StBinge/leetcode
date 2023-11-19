#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=[0]*26
        for ch in magazine:
            cnt[ord(ch)-ord('a')]+=1
        for ch in ransomNote:
            id=ord(ch)-ord('a')
            if cnt[id]==0:
                return False
            cnt[id]-=1
        return True
# @lc code=end
