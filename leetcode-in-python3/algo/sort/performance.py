from typing import List, Callable
import helper
import time
from insert_sort import insert_sort
from select_sort import select_sort
from quick_sort import quick_sort


def algo_performance(algos: List[Callable[[List[int]], None]], size, l, r):
    arr = helper.random_nums(size, l, r)
    for fn in algos:
        nums = arr[:]
        start = time.time()
        fn(nums)
        end = time.time() - start
        print(f"{fn.__name__}: {end} s")


algo_performance([select_sort, insert_sort, quick_sort], 1000, 0, 1)
