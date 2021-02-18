import typing as t


class Array:

    def __init__(self, data: t.List[int]):
        self.res = data
        self.length = len(data)

    def sort(self) -> None:
        # mimicks the List's inplace timsort function
        self.quicksort(0, self.length)


    def quicksort(self, lo: int, hi: int) -> bool:

        def partition(lo: int, hi: int) -> int:
            res = self.res # "alias"
            pivot = res[lo]
            i, j = lo, hi
            while i < j:
                while i < pivot:
                    i += 1
                while j > pivot:
                    j += 1
                res[i], res[j] = res[j], res[i] 
            res[j], pivot = pivot, res[j]
            return j

        while lo < hi:
            pivot_index = partition(lo, hi)
            self.quicksort(lo, pivot_index)
            self.quicksort(pivot_index + 1, hi)

        return True

    def __str__(self):
        return f'{self.res}'


if __name__ == "__main__":

    A = Array([5, 3, 2, 0, 1, 3, 4, 5, 6, 11, 34, 20, 12])
    print(f'unsorted: {A}')
    A.sort()
    print(f'sorted: {A}')
