import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

# strat: write ordinary QS then adapt so that swapping of pivot shifts range of all values equal to pivot

# demo out of place one liner
# qs= lambda l: qs([i for i in l if i<l[len(l)//2]])+[i for i in l if i==l[len(l)//2]]+qs([i for i in l if i>l[len(l)//2]]) if l else []

# regular quick sort partition
# def qs(p, A):
#     pv=A[p]
#     i=0
#     s=0
#     while i<p:
#         el = A[i]
#         print(el)
#         if el>pv:
#             A[i], A[p], A[p-1] = A[p-1] , A[i], A[p]
#             p-=1
#             s+=1
#         else:
#             i+=1
#     i=p+s
#     while i<len(A):
#         el=A[i]
#         if el<pv:
#             A[p], A[p+1:i+1] = A[i], A[p:i]
#             p+=1
#         else:
#             i+=1

# slices to shift and check ==pivot value
# def qs(p, A):
#     pv=A[p]
#     i=0
#     s=0
#     pe=p
#     while i<p:
#         el = A[i]
#         print(el)
#         if el>pv:
#             A[i], A[pe], A[p-1:pe] = A[p-1], A[i], A[p:pe+1]
#             p-=1
#             pe-=1
#             s+=1
#         elif el==pv:
#             A[i], A[p+1], A[p+2:pe+2]=A[pe+1], A[i], A[p+1:pe+1]
#             s+=1
#             pe+=1

#         else:
#             i+=1
#     i=pe+s
#     while i<len(A):
#         el=A[i]
#         if el<pv:
#             A[p], A[p+1:i+1] = A[i], A[p:i]
#             p+=1
#             pe+=1
#         elif el==pv:
#             A[p+1], A[p+2:i+1]  = A[i], A[p+1:i]
#             pe+=1
#         else:
#             i+=1
#     print(i, pe)

# full recursive quicksort
def qs(p, b, e, A):
    width = e - b
    if width <= 0:
        return
    elif width == 1:
        A[b], A[e] = min(A[b], A[e]), max(A[b], A[e])
        return
    pv = A[p]
    i = b
    s = 0
    pe = p
    while i < p:
        el = A[i]
        if el > pv:
            A[i], A[pe], A[p - 1 : pe] = A[p - 1], A[i], A[p : pe + 1]
            p -= 1
            pe -= 1
            s += 1
        elif el == pv:
            A[i], A[p + 1], A[p + 2 : pe + 2] = A[pe + 1], A[i], A[p + 1 : pe + 1]
            s += 1
            pe += 1

        else:
            i += 1
    i = pe + s
    while i <= e:
        el = A[i]
        if el < pv:
            A[p], A[p + 1 : i + 1] = A[i], A[p:i]
            p += 1
            pe += 1
        elif el == pv:
            A[p + 1], A[p + 2 : i + 1] = A[i], A[p + 1 : i]
            pe += 1
        else:
            i += 1
    qs((b + p - 1) // 2, b, p - 1, A), qs((pe + 1 + e) // 2, pe + 1, e, A)


def swap(l: list, a: int, b: int) -> None:
    """
    Args:
        l: list to swap in
        a: index of first element
        b: index of second element
    Returns:
        None
    simple helper to swap in list l indices a and b
    """
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def shift_elements(a: list, s: int, e: int, p: int) -> list:
    """
    Quicksort partitioning function. The heart of quicksort. Allows arbitrary pivot.
    Uses Dutch National Flag Style Partitioning:
    partition the array a so that all elements equal to p are contiguous around p
    all elements less than p are left of said contiguous region 
    and all elements greater than p are right of said contiguous region
    Args:
        a: list to partition
        s: index start range of partitioning
        e: index end range of partitioning
        p: index pivot to partition around
    Returns:
        a sorted inplace
    """
    # if the start and end have passed one another we stop
    if s >= e:
        return
    # some sanity checkers
    assert s <= p <= e, "Invalid Pivot"
    assert s < e, f"Invalid start: {s} and end: {e}. Must have Start<=End."
    # c counts how many times we've appended to the right working on the left half
    c = 0
    # i is the current index we're looking at
    i = 0
    # bp will keep track of the pivot moving left as a result of appending
    # when we move begin to move from the right it will give us where the pivot is after we moved from the left
    # after we've been moving it
    bp = p
    # we start on the left
    while i < p:
        # if we the current element is greater value than pivot it needs to be moved to after it (here we move to end of cur range e)
        if a[i] > a[p]:
            a.insert(e + 1, a[i])
            del a[i]
            p -= 1
            bp -= 1
            c += 1
        # equal elements from the left will be juxtaposed with the pivot to the left
        # we'll use this as the new pivot for the time being so continue to juxtapose further equal elements we encounter
        elif a[i] == a[p]:
            swap(a, i, p - 1)
            p -= 1  # note no change to bp as this is not the original pivot
        # if the element is less than the pivot value we dont need to do anything and just move to the next index
        else:

            i += 1
    # just before where the contiguous region starts
    # is the end of the left partition
    left_end = p - 1
    # we could start at e but we already know that the c elements we appended are in the right spot for this partitioning
    i = -c + e
    # remind p to be the original pivot
    p = bp
    # we do the same thing as above except from the right
    while i > p:
        # move elements that are less than the pivot's value to the start of this partitioning s
        if a[i] < a[p]:
            a.insert(s, a[i])
            del a[i + 1]
            p += 1
        # contiguous region extending to the right this time instead of left
        elif a[i] == a[p]:
            swap(a, i, p + 1)
            p += 1
        else:
            i -= 1
    # from above we made the left_end after working from the left
    # it has moved now since working from the right having appended new elements less than pivot value to the left start
    # so we need to move it over by this number that we have appended
    left_end += p - bp
    # the new left start is just the current start
    left_start = s
    # the new right end is just the current end
    right_end = e
    right_start = p + 1

    # recurse left and right
    shift_elements(a, left_start, left_end, left_start + (left_end - left_start) // 2)
    shift_elements(
        a, right_start, right_end, right_start + (right_end - right_start) // 2
    )

    return a


def sol(p: int, l: list) -> list:
    """
    inplace quicksort
    Args:
        l: list to sort inplace
    Returns:
        l sorted inplace
    """
    if len(l) < 2:
        return l
    return shift_elements(l, 0, len(l) - 1, len(l) // 2)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    sol(pivot_index, A)


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure("Not partitioned after {}th element".format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "dutch_national_flag.py",
            "dutch_national_flag.tsv",
            dutch_flag_partition_wrapper,
        )
    )
