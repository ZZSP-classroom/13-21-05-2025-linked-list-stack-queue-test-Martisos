class Queue:
    def __init__(self) -> None:
        self.lista = []
    
    def sort(self):
        self.lista.sort(key=lambda task: task.priority)

    def enqueue(self, object):
        self.lista.append(object)
        self.sort()

    def dequeue(self):
        if len(self.lista) > 0:
            return self.lista.pop(0)

    def peek(self):
        if len(self.lista) > 0:
            return self.lista[0]


class Task:
    def __init__(self, task_name, priority) -> None:
        self.task_name = task_name
        self.priority = priority
