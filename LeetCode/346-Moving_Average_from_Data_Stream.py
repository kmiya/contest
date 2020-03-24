# circular queue solution
# time: O(1)
# space: O(size)


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.capacity = size
        self.rear = 0
        self.size = 0
        self.queue = [0] * size
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum = self.sum - self.queue[self.rear] + val
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity
        self.size = min(self.size + 1, self.capacity)
        return self.sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
