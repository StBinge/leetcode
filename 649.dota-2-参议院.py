#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=deque()
        dire=deque()
        for i,side in enumerate(senate):
            if side=='R':
                radiant.append(i)
            if side=='D':
                dire.append(i)
        L=len(senate)
        while radiant and dire:
            if radiant[0]<dire[0]:
                dire.popleft()
                radiant.append(radiant.popleft()+L)
            else:
                radiant.popleft()
                dire.append(dire.popleft()+L)
        if len(radiant):
            return 'Radiant'
        else:
            return 'Dire'

        

# @lc code=end

assert Solution().predictPartyVictory('RD')=='Radiant'
assert Solution().predictPartyVictory('RDD')=='Dire'