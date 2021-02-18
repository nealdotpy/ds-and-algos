import typing as t


class Array:

    def __init__(self, data: t.List[int]):
        self.res = data
        self.length = len(data)

    def sort(self) -> None:
        # mimicks the List's inplace timsort function
        self.quicksort(0, self.length - 0)


    def quicksort(self, lo: int, hi: int) -> bool:

        if lo < hi:
            pivot_index = self.partition_pythonic(lo, hi)
            self.quicksort(lo, pivot_index)
            self.quicksort(pivot_index + 1, hi)

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


if __name__ == "__main__":

    A = Array([5, 3, 2, 0, 1, 25, 21, 18, 8])
    D = Array([5, 3, 2, 0, 1, 3, 4, 5, 6, 11, 34, 20, 12])

    test_cases = [A, D]

    for case in test_cases:
        print(f'unsorted: {case} ({case.length})')
        case.sort()
        print(f'sorted: {case}')
