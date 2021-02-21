#include<iostream>
#include<array>
#include<cstddef>
#include<vector>

// using namespace std;

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void printArray(std::vector<int> array) {
	for (auto n: array) {
		std::cout << n << " ";
	}
	std::cout << std::endl;
}

int partition(std::vector<int>* array, int lo, int hi) {
	int pivot = (*array)[lo];
	int i = lo;
	int j = hi;
	while (i < j) {
		do {
			i++;
		} while ((*array)[i] < pivot);
		do {
			j--;
		} while ((*array)[j] > pivot);
		if (i < j) {
			swap(&(*array)[i], &(*array)[j]);
		}
	}
	swap(&(*array)[j], &(*array)[lo]);
	return j;
}

void quicksort(std::vector<int>* array, int lo, int hi) {
	if (lo < hi) {
		int pivotIndex = partition(array, lo, hi);
		quicksort(array, lo, pivotIndex);
		quicksort(array, pivotIndex + 1, hi);
	}
}

// void test(std::vector<int>* vec) {
// 	(*vec)[0] = -1;
// }

int main() {

	std::vector<std::vector<int>> testCases {
		{0, 2, 7, 49, 4},
		{2, 10, 20, 94, 28, 8, 34, 64, 31, 1},
		{20, 94, 28, 8, 34, 64, 0, 2, 7, 49, 4, 7, 5, 2, 98}
	};

	// std::cout << testCases[0][0] << std::endl;
	// test(&testCases[0]);
	// std::cout << testCases[0][0] << std::endl;

	for (auto tCase: testCases) {
		std::cout << "sorting: ";
		printArray(tCase);
		quicksort(&tCase, 0, tCase.size());
		std::cout << "sorted: ";
		printArray(tCase);
	}

	return 0;

}