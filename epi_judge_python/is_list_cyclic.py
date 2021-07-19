import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

node_eq=lambda a, b: id(a)==id(b)

def iter_list(s, step=1, stop_on_cycle=False):
#     import pdb; pdb.set_trace()
    l=s
    first=True
    while (l is not None) and ( not (node_eq(l, s) and not first) if stop_on_cycle else True):
        first=False
        yield l
        for _ in range(step):
            try:
                l=l.next
            except AttributeError:
                l=None

def has_cycle(s: ListNode) -> Optional[ListNode]:
    # import pdb; pdb.set_trace()
    cycle=False
    if not(s and s.next):
        return None
    for a, b in zip(iter_list(s, 1), iter_list(s.next, 2)):
        if node_eq(a, b):
            cycle=True
            break
    if not cycle:
        return None
    cycle_len=sum(1 for _ in iter_list(a, stop_on_cycle=True))
    follower=a
    leader=a
    for _ in range(cycle_len):
        leader=leader.next
    for a, b in zip(iter_list(follower), iter_list(leader)):
        if node_eq(a, b):
            return a


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", "is_list_cyclic.tsv", has_cycle_wrapper
        )
    )
