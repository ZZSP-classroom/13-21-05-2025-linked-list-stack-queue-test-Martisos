import unittest
from call_center_4 import *

class BasicCase(unittest.TestCase):
    def testEnqueue(self):
        q = Queue()

        c1 = Call(1, "14:09:20")
        c2 = Call(2, "20:09:20")

        q.enqueue(c1)
        q.enqueue(c2)

        self.assertEqual(q.peek(), c1)
    
    def testDequeue(self):
        q = Queue()

        c1 = Call(1, "14:09:20")
        c2 = Call(2, "20:09:20")

        q.enqueue(c1)
        q.enqueue(c2)

        q.dequeue()

        self.assertEqual(q.peek(), c2)

    def testPush(self):
        s = Stack()

        c1 = Call(1, "14:09:20")
        c2 = Call(2, "20:09:20")

        s.push(c1)
        s.push(c2)

        self.assertEqual(s.peek(), c2)

    def testPop(self):
        s = Stack()

        c1 = Call(1, "14:09:20")
        c2 = Call(2, "20:09:20")

        s.push(c1)
        s.push(c2)

        s.pop()

        self.assertEqual(s.peek(), c1)


if __name__ == "__main__":
    unittest.main()