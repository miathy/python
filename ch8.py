class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return (len(self.q) ==0)
    def enqueue(self, item):
        return self.q.append(item)
    def dequeue(self):
        return self.q.pop(0)