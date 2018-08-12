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
	sorted_arr := BubbleSort(arr)
	fmt.Println(sorted_arr)
	Test(arr, sorted_arr)
}

func BubbleSort(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := len(arr) - 1; j > i; j-- {
			if arr[j] < arr[j-1] {
				arr[j], arr[j-1] = arr[j-1], arr[j]
			}
		}
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
