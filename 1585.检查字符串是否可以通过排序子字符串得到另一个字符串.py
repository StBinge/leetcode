#
# @lc app=leetcode.cn id=1585 lang=python3
#
# [1585] 检查字符串是否可以通过排序子字符串得到另一个字符串
#


# @lc code=start
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        N=len(s)
        pos=[[] for _ in range(10)]

        for i in range(N-1,-1,-1):
            pos[int(s[i])].append(i)

        
        for i in range(N):
            num=int(t[i])
            if not pos[num]:
                return False
            j=pos[num].pop()
            for k in range(num):
                if pos[k] and pos[k][-1]<j:
                    return False                
        return True

# @lc code=end

assert Solution().isTransformable(s = "1", t = "2") == False
assert Solution().isTransformable("432513576","231435567")
assert Solution().isTransformable(s="12345", t="12435") == False
assert Solution().isTransformable(s="34521", t="23415")
assert Solution().isTransformable(s="84532", t="34852")
