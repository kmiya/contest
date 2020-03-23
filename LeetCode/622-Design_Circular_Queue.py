# simple array solution (thread-safe)
# time: O(1)
# space: O(k)

from threading import Lock


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.front = 0
        self.rear = 0
        self.queue = [None] * k
        self.lock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        with self.lock:
            if self.isFull():
                return False
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        with self.lock:
            if self.isEmpty():
                return False
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        value = self.queue[self.front]
        if value is None:
            return -1
        return value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        value = self.queue[(self.rear - 1) % self.size]
        if value is None:
            return -1
        return value

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.queue[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.queue[self.rear] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
