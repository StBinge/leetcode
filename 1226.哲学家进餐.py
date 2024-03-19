#
# @lc app=leetcode.cn id=1226 lang=python3
#
# [1226] 哲学家进餐
#

# @lc code=start
from threading import Lock,Semaphore
class DiningPhilosophers:
    def __init__(self) -> None:
        self.limit=Semaphore(4)
        self.locks=[Lock() for _ in range(5)]
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.limit.acquire()
        left_fork=philosopher
        right_fork=(philosopher+1)%5
        self.locks[left_fork].acquire()
        self.locks[right_fork].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.locks[right_fork].release()
        self.locks[left_fork].release()
        self.limit.release()
        
# @lc code=end

