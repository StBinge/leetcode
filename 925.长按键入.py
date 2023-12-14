#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#


# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0]:
            return False
        i1, i2 = 1, 1
        l1, l2 = len(name), len(typed)
        while i1 < l1 and i2 < l2:
            if name[i1] == typed[i2]:
                i1 += 1
                i2 += 1
            elif typed[i2] == typed[i2 - 1]:
                i2 += 1
            else:
                return False
        while i2 < l2 and typed[i2] == typed[i2-1]:
            i2 += 1
        return i1 == l1 and i2 == l2


# @lc code=end
name = "alex"
typed = "aaleexa"
assert Solution().isLongPressedName(name, typed) == False

name = "vtkgn"
typed = "vttkgnn"
assert Solution().isLongPressedName(name, typed) == True


name = "saeed"
typed = "ssaaedd"
assert Solution().isLongPressedName(name, typed) == False

name = "alex"
typed = "aaleex"
assert Solution().isLongPressedName(name, typed)
