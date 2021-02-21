import typing as t
from random import randint


class Array:

    def __init__(self, data: t.List[int]):
        self.unsorted = data
        self.res = data
        self.length = len(data)

    def sort(self) -> None:
        # mimicks the List's inplace timsort function
        self.r_quicksort(0, self.length - 0)


    def r_quicksort(self, lo: int, hi: int) -> bool:

        if lo < hi:
            pivot_index = self.partition_pythonic(lo, hi)
            self.r_quicksort(lo, pivot_index)
            self.r_quicksort(pivot_index + 1, hi)

        return True

    def partition_non_pythonic(self, lo: int, hi: int) -> int:
        pivot = self.res[lo]
        i, j = lo, hi
        while i < j:
            while 1:
                i += 1
                if i >= self.length:
                    break 
                if self.res[i] > pivot:
                    break
            while 1:
                j -= 1
                if j < 0:
                    break
                if self.res[j] <= pivot:
                    break
            if i < j:
                self.res[i], self.res[j] = self.res[j], self.res[i]
        self.res[j], self.res[lo] = self.res[lo], self.res[j]
        return j

    def partition_pythonic(self, lo: int, hi: int) -> int:
        rand_idx = randint(lo, hi - 1)
        self.res[lo], self.res[rand_idx] = self.res[rand_idx], self.res[lo]
        pivot = self.res[lo]
        i, j = lo, hi
        while i < j:
            i, j = i + 1, j - 1
            while i < self.length and self.res[i] <= pivot:
                i += 1
            while j >= 0 and self.res[j] > pivot:
                j -= 1
            if i < j:
                self.res[i], self.res[j] = self.res[j], self.res[i]
        self.res[j], self.res[lo] = self.res[lo], self.res[j]
        return j


    def __str__(self):
        return f'{self.res}'



class T:
    NUM_RANGE = 1001
    NUM_COUNT = 300


if __name__ == "__main__":

    test_cases = [
        Array([5, 3, 2, 0, 1, 25, 21, 18, 8]),
        Array([5, 3, 2, 0, 1, 3, 4, 5, 6, 11, 34, 20, 12]),
        Array([randint(0, T.NUM_RANGE) for i in range(T.NUM_COUNT)])
    ]

    for i, case in enumerate(test_cases):
        print(f'sorting case{i}[{case.length}]...')
        case.sort()
        #case.unsorted.sort() # timsort -> verifies the sorted status
        equiv = case.res == sorted(case.unsorted)
        print(f'{"SUCCESS" if equiv else "FAILURE"} case{i}[{case.length}].')
       