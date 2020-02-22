#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ylgongPw @ 2020-02-22 15:46:14

class MyCircularQueue:

    def __init__(self,k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.count = 0
        self.items = [0] * k
        self.length = k
        self.head_index = 0


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            self.items[(self.head_index+self.count) % self.length] = value
            self.count += 1
            return True
        else:
            return False


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.head_index = (self.head_index + 1) % self.length
            self.count -= 1
            return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[self.head_index]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.items[(self.head_index+self.count-1) % self.length]


    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.length


if __name__ == '__main__':
    obj = MyCircularQueue(3)
    print (obj.enQueue(1))
    print (obj.enQueue(2))
    print (obj.enQueue(3))
    print (obj.enQueue(4))
    print (obj.Rear())
    print (obj.isFull())
    print (obj.deQueue())
    print (obj.enQueue(4))
    print (obj.Rear())
