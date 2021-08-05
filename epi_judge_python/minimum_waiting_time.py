from typing import List

from test_framework import generic_test

from functools import reduce
def minimum_total_waiting_time(service_times: List[int]) -> int:
    ret=0
    prev=0
    for i in sorted(service_times)[:-1]:
        prev+=i
        ret+=prev
    return ret

if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "minimum_waiting_time.py",
            "minimum_waiting_time.tsv",
            minimum_total_waiting_time,
        )
    )
