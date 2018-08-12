package main

import (
	"math/rand"
	"fmt"
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
	val := arr[rand.Intn(len(arr))]
	fmt.Println(SequentialSearch(arr, val))
}

func SequentialSearch(arr []int, val int) (int, int) {
	for i := 0; i < len(arr); i++ {
		if arr[i] == val {
			return i, val
		}
	}
	return 0, 0
}
