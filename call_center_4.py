from typing import List

class Queue:
    def __init__(self):
        self._List: List = []
    
    def enqueue(self, item):
        self._List.append(item)

    def dequeue(self):
        if(len(self._List) > 0):
            return self._List.pop(0)
        else:
            return None
    
    def peek(self):
        if(len(self._List) > 0):
            return self._List[0]
        else:
            return None
    
class Stack:
    def __init__(self):
        self._List = []

    def push(self, item):
        self._List.append(item)

    def pop(self):
        if(len(self._List) > 0):
            return self._List.pop()
        else:
            return None
    
    def peek(self):
        if(len(self._List) > 0):
            return self._List[-1]
        else:
            return None
        


class Call:
    def __init__(self, caller_id: int, time_recived: str):
        self.caller_id = caller_id
        self.time_recived = time_recived