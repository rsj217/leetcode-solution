package sort

import "testing"

func TestAlgoRandomPerformance(t *testing.T) {
	algos := []Algo{
		{"SelectSort", SelectSort},
		{"InsertSort", InsertSort},
		{"QuickSort", QuickSort},
		{"MergeSort", MergeSort},
	}
	AlgoRandomPerformance(algos, 100000, 0, 10000)
}

func TestAlgoNearlyOrderPerformance(t *testing.T) {
	algos := []Algo{
		{"InsertSort", InsertSort},
		{"QuickSort", QuickSort},
		{"MergeSort", MergeSort},
	}
	AlgoNearlyOrderPerformance(algos, 100000, 10)
}
