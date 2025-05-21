class Queue:
    def __init__(self) -> None:
        self.lista = []
    
    def enqueue(self, object):
        self.lista.append(object)

    def dequeue(self):
        if len(self.lista) > 0: 
            return self.lista.pop(0)

    def peek(self):
        if len(self.lista) > 0:
            return self.lista[0]

class Patient:
    def __init__(self, name, appointment_time) -> None:
        self.name = name
        self.appointment_time = appointment_time