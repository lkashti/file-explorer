
class NavigationStack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def push(self, path):
        self.stack.append(path)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]

    def clear_stack(self):
        self.stack.clear()

