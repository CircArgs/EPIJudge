import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s) -> int:
    b_s, a_s=0,0
    for i in range(size):
        t=s[i]
        if t=='a':
            a_s+=1
        elif t=='b':
            b_s+=1
#     print(b_s, a_s)
    tracker=size-1
    final_size=size-b_s+2*a_s
    i=final_size-1
#     import pdb; pdb.set_trace()
    while tracker>=0:
        # print(tracker, i)
        temp=s[tracker]
        if temp=='b':
            tracker-=1
        elif temp=='a':
            s[i-1], s[i]='dd'
            i-=2
            tracker-=1
        else:
            s[i]=s[tracker]
            i-=1
            tracker-=1
#     for i in range(len(s)):
#         if s[i]!='b':
#             break
    
    del s[final_size:]
    del s[:i+1]
    return final_size
    


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
