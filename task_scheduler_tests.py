import unittest
import task_scheduler_5

class testText(unittest.TestCase):

    def testAddTask(self):
        queue = task_scheduler_5.Queue()
        task1 = task_scheduler_5.Task("task01", 1)
        task2 = task_scheduler_5.Task("task02", 2)
        task3 = task_scheduler_5.Task("task01", 0)

        queue.enqueue(task1)
        queue.enqueue(task2)
        queue.enqueue(task3)

        self.assertNotEqual([], queue.lista)

    def testProcess(self):
        queue = task_scheduler_5.Queue()
        task1 = task_scheduler_5.Task("task01", 1)
        task2 = task_scheduler_5.Task("task02", 2)
        task3 = task_scheduler_5.Task("task01", 0)

        queue.enqueue(task1)
        queue.enqueue(task2)
        queue.enqueue(task3)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        self.assertEqual([], queue.lista)

if __name__ == "__main__":
    unittest.main()