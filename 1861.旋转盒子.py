#
# @lc app=leetcode.cn id=1861 lang=python3
#
# [1861] 旋转盒子
#
from sbw import *
# @lc code=start
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R,C=len(box),len(box[0])
        ret=[['.']*R for _ in range(C)]
        for r in range(R):
            bottom=C-1
            col=R-1-r
            for c in range(C-1,-1,-1):
                ch=box[r][c]
                if ch=='#':
                    if c<bottom:
                        ret[bottom][col]='#'
                        bottom-=1
                    else:
                        ret[c][col]='#'
                        bottom=c-1
                elif ch=='*':
                    ret[c][col]='*'
                    bottom=c-1
        return ret

# @lc code=end
assert Solution().rotateTheBox([["#","#","*",".","*","."],
            ["#","#","#","*",".","."],
            ["#","#","#",".","#","."]])==[[".","#","#"],
      [".","#","#"],
      ["#","#","*"],
      ["#","*","."],
      ["#",".","*"],
      ["#",".","."]]
assert Solution().rotateTheBox([["#",".","*","."],
            ["#","#","*","."]])==[["#","."],
      ["#","#"],
      ["*","*"],
      [".","."]]

assert Solution().rotateTheBox( [["#",".","#"]])==[["."],
      ["#"],
      ["#"]]
