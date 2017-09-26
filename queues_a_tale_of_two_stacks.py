class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def _from_one_to_another(self, stack_from, stack_to):
        while len(stack_from) > 0:
            stack_to.append(stack_from.pop())

    def peek(self):
        if len(self.second) == 0:
            if len(self.first) == 0:
                return None
            else:
                self._from_one_to_another(self.first, self.second)
        return self.second[-1]

    def pop(self):
        if len(self.second) == 0:
            self._from_one_to_another(self.first, self.second)
        return self.second.pop()

    def put(self, value):
        self.first.append(value)


queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())

    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
