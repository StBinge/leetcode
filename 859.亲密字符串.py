#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        swapped=-1
        vis=set()
        repeated=False
        for i,sc in enumerate(s):
            if not repeated:
                if sc in vis:
                    repeated=True
                else:
                    vis.add(sc)
            if sc==goal[i]:
                continue
            if swapped==-1:
                swapped=i
            elif swapped==len(s):
                return False
            elif s[i]==goal[swapped] and s[swapped]==goal[i]:
                swapped=len(s)
            else:
                return False
        
        return swapped==len(s) or (swapped==-1 and repeated)
# @lc code=end

s = "ab"
goal = "ba"
assert Solution().buddyStrings(s,goal)
assert Solution().buddyStrings('ab','ab')==False
assert Solution().buddyStrings('aa','aa')==True
assert Solution().buddyStrings('abab','abab')==True
assert Solution().buddyStrings('abac','abad')==False