import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

def gasup(g, d):
    return sorted(list(enumerate(zip(g, d))), key=lambda x: x[1][0]*MPG, reverse=True)

def check(s, gas, distances):
    s, (g, d) = s
    i=(s+1)%len(gas)
    miles = g*MPG
    while i!=s:
        miles-=distances[i-1]
        if miles<0:
            return False
        miles+=gas[i]*MPG
        i=(i+1)%len(gas)
    return True



def cum(f, it, start=0):
    for i in it:
        start=f(start, i)
        yield start
        
def gasup(g, d):
    return (min(enumerate(cum(lambda x, y: x+MPG*y[0]-y[1], zip(g, d))), key=lambda x: x[-1])[0]+1)%len(g)

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    return gasup(gallons, distances)


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure("Out of gas on city {}".format(i))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "refueling_schedule.py", "refueling_schedule.tsv", find_ample_city_wrapper
        )
    )
