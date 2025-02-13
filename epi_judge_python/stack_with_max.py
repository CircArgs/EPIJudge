from test_framework import generic_test
from test_framework.test_failure import TestFailure


class MaxStore:
    def __init__(self):
        self.store = []

    @property
    def max(self) -> int:
        if self.store:
            return self.store[-1][0]
        return float("-inf")

    def push(self, x: int):
        if self.max < x:
            self.store.append([x, 1])
        elif x == self.max:
            self.store[-1][1] += 1

    def pop(self):
        if self.store[-1][1] == 1:
            return self.store.pop()[0]
        else:
            self.store[-1][1] -= 1
            return self.store[-1][0]


class Stack:
    def __init__(self):
        self.store = []
        self.max_store = MaxStore()

    def empty(self) -> bool:
        return not self.store

    def max(self) -> int:
        if self.empty():
            return 0
        return self.max_store.max

    def pop(self) -> int:
        self.max_store.pop()
        return self.store.pop()

    def push(self, x: int):
        if self.empty():
            self.max_store.push(x)
        else:
            if x > self.max():
                self.max_store.push(x)
            else:
                self.max_store.push(self.max())
        self.store.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == "Stack":
                s = Stack()
            elif op == "push":
                s.push(arg)
            elif op == "pop":
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "max":
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result)
                    )
            elif op == "empty":
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result)
                    )
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure("Unexpected IndexError exception")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "stack_with_max.py", "stack_with_max.tsv", stack_tester
        )
    )
