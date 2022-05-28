package main

import (
	"fmt"
	"math"
)

func main() {
	size := 26
	tt := make([]int, size)
	for i := 1; i <= size; i++ {
		tt[i-1] = i
	}
	sum := 0
	for _, s := range PowerSet(tt) {
		for _, v := range s {
			sum += v
		}
	}
	fmt.Println(sum)
}

func PowerSet(nums []int) [][]int {
	powerSetSize := int(math.Pow(2, float64(len(nums))))
	subsets := make([][]int, 0, powerSetSize)
	var index int
	for index < powerSetSize {
		var subSet []int
		for i, num := range nums {
			if index&(1<<uint(i)) > 0 {
				subSet = append(subSet, num)
			}
		}
		subsets = append(subsets, subSet)
		index++
	}
	return subsets
}

