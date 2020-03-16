# time: O(N)
# space: O(N)
# Runtime: 40 ms, faster than 51.99% of Python3 online submissions for Read N Characters Given Read4 II - Call multiple times.
# Memory Usage: 13.1 MB, less than 6.15% of Python3 online submissions for Read N Characters Given Read4 II - Call multiple times.


class Solution:
    def __init__(self):
        self.read_buffer_ = []
        self.read_ptr_ = -1
        self.used_ptr_ = 0

    def read(self, buf, n):
        buf[:] = []
        res = n
        while len(buf) < n:
            if self.read_ptr_ < self.used_ptr_ and res > 0:
                tmp = [' '] * 4
                rnum = read4(tmp)
                if not rnum: break
                self.read_buffer_ += tmp[:rnum]
                self.read_ptr_ += rnum
            buf += self.read_buffer_[self.used_ptr_]
            self.used_ptr_ += 1
            res -= 1
        return len(buf)
