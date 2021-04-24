package sort

import (
	"fmt"
	"leetcode/util"
	"time"
)

func timeCost() func() {
	start := time.Now()
	return func() {
		tc := time.Since(start)
		fmt.Printf("time cost = %v\n", tc)
	}
}

type Algo struct {
	Name     string
	SortFunc func([]int)
}

func AlgoRandomPerformance(algos []Algo, size, l, r int) {
	arr := util.RandomNums(size, l, r)
	nums := make([]int, len(arr))
	for _, algo := range algos {
		copy(nums, arr)
		func() {
			fmt.Printf("%s ", algo.Name)
			defer timeCost()()
			algo.SortFunc(nums)
		}()
	}
}

func AlgoNearlyOrderPerformance(algos []Algo, size, swap int) {
	arr := util.RandomNearlyOrderNums(size, swap)
	nums := make([]int, len(arr))
	for _, algo := range algos {
		copy(nums, arr)
		func() {
			fmt.Printf("%s ", algo.Name)
			defer timeCost()()
			algo.SortFunc(nums)
		}()
	}
}
