#include<iostream>
#include<array>
#include<cstddef>
#include<vector>

// using namespace std;

int partition(int* array, int lo, int hi) {
	int pivot = array[lo];
	return 0;
}

int quicksort(int* array, int lo, int hi) {
	if (lo < hi) {
		int pivotIndex = partition(array, lo, hi);
		quicksort(array, lo, pivotIndex);
		quicksort(array, pivotIndex + 1, hi);
	}
	return 1;
}

void printArray(std::vector<int> array) {
	for (auto n: array) {
		std::cout << n << " ";
	}
	std::cout << std::endl;
}

int main() {

	std::vector<std::vector<int>> testCases {
		{0, 2, 7, 49, 4},
		{2, 10, 20, 94, 28, 8, 34, 64, 31, 1},
		{20, 94, 28, 8, 34, 64, 0, 2, 7, 49, 4, 7, 5, 2, 98}
	};

	for (auto tCase: testCases) {
		std::cout << "sorting: ";
		printArray(tCase);
		// quicksort(tCase);
		std::cout << "sorted: ";
		printArray(tCase);
	}

	return 0;

}