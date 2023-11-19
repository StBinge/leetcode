#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        nodes=preorder.split(',')
        N=len(nodes)
        slots=1
        idx=0
        while idx<N:
            if not slots:
                return False
            slots-=1
            if nodes[idx]!='#':
                slots+=2
            idx+=1
        return slots==0
# @lc code=end
assert Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
assert Solution().isValidSerialization("9,#,#,1")==False


assert Solution().isValidSerialization("1,#")==False