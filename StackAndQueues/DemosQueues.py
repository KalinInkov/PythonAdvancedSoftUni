class Queue:
    def __init__(self):
        self.internal_values=[]
        self.start_index = 0
        self.queue_size = 0

    def enqueue(self,value):
        self.internal_values.append(value)
        self.queue_size+=1
    def deque(self):
        value=self.internal_values[self.start_index]
        self.start_index+=1
        self.queue_size -= 1
        return value

    def peek(self):
        return self.internal_values[self.start_index]

    @property
    def is_empty(self):
        return self.queue_size==0

q = Queue()

[q.enqueue(x) for x in range(5)]

while not q.is_empty:
    print(q.deque())

