#
# @lc app=leetcode.cn id=2526 lang=python3
# @lcpr version=30204
#
# [2526] 找到数据流中的连续整数
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class DataStream:

    def __init__(self, value: int, k: int):
        self.cnt = 0
        self.target = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.target:
            self.cnt += 1
        else:
            self.cnt = 0
        return self.cnt >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
# @lc code=end
obj = DataStream(4, 3)
ops = ["DataStream", "consec", "consec", "consec", "consec"]
args = [[4, 3], [4], [4], [4], [3]]
ret = "[null, false, false, true, false]"
test_obj(obj, ops, args, ret)


#
# @lcpr case=start
# ["DataStream", "consec", "consec", "consec", "consec"][[4, 3], [4], [4], [4], [3]]\n
# @lcpr case=end

#
