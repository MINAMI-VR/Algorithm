package main

import (
	"math/rand"
	"fmt"
	"sort"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	length := rand.Intn(10) + 10
	arr := make([]int, length)
	for i := 0; i < len(arr); i++ {
		arr[i] = rand.Intn(100)
	}
	fmt.Println(arr)
	sorted_arr := SelectSort(arr)
	fmt.Println(sorted_arr)
	Test(arr, sorted_arr)
}

func SelectSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		min_i := i
		for j := i + 1; j < len(arr); j++ {
			if arr[min_i] > arr[j] {
				min_i = j
			}
		}
		tmp := arr[min_i]
		for j := min_i; i < j; j-- {
			arr[j] = arr[j-1]
		}
		arr[i] = tmp
	}
	return arr
}

func Test(arr, sorted_arr []int) bool {
	sort.Ints(arr)
	for i := 0; i < len(arr); i++ {
		if arr[i] != sorted_arr[i] {
			fmt.Println("False")
			return false
		}
	}
	fmt.Println("True")
	return true
}
