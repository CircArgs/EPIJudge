from test_framework import generic_test
ops={'*', '-', '+', '/'}
def ev(l):
    stack=[0]
    for e in l:
        if e in ops:
            a, b = stack.pop(), stack.pop()
            stack.append(int(eval(f'{b}{e}{a}')))
        else:
            stack.append(e)
    return int(stack[-1])

def evaluate(s: str) -> int:
    return ev(s.split(','))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", "evaluate_rpn.tsv", evaluate)
    )
