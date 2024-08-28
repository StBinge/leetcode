#
# @lc app=leetcode.cn id=1845 lang=python3
#
# [1845] 座位预约管理系统
#
from sbw import *
# @lc code=start
class SeatManager:

    def __init__(self, n: int):
        self.seats=[i for i in range(1,n+1)]
        heapq.heapify(self.seats)


    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end

seatManager = SeatManager(5); # 初始化 SeatManager ，有 5 个座位。
assert seatManager.reserve()==1;    # 所有座位都可以预约，所以返回最小编号的座位，也就是 1 。
assert seatManager.reserve()==2;    # 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
seatManager.unreserve(2); # 将座位 2 变为可以预约，现在可预约的座位为 [2,3,4,5] 。
assert seatManager.reserve()==2;    # 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
assert seatManager.reserve()==3;    # 可以预约的座位为 [3,4,5] ，返回最小编号的座位，也就是 3 。
assert seatManager.reserve()==4;    # 可以预约的座位为 [4,5] ，返回最小编号的座位，也就是 4 。
assert seatManager.reserve()==5;    # 唯一可以预约的是座位 5 ，所以返回 5 。
seatManager.unreserve(5); # 将座位 5 变为可以预约，现在可预约的座位为 [5] 。