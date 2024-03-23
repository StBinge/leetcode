#
# @lc app=leetcode.cn id=1117 lang=python3
#
# [1117] H2O 生成
#

# @lc code=start
from threading import Semaphore,Lock
class H2O:
    def __init__(self):
        self.olock=Semaphore(1)
        self.hlock=Semaphore(2)
        self.lock=Lock()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hlock.acquire()
        releaseHydrogen()
        with self.lock:
            if self.olock._value==0 and self.hlock._value==0:
                self.hlock.release()
                self.hlock.release()
                self.olock.release()

        # releaseHydrogen() outputs "H". Do not change or remove this line.


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.olock.acquire()
        releaseOxygen()
        with self.lock:
            if self.olock._value==0 and self.hlock._value==0:
                self.hlock.release()
                self.hlock.release()
                self.olock.release()
# @lc code=end

