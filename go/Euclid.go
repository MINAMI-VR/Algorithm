package main

import (
	"math/rand"
	"time"
	"fmt"
	"math/big"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	a := rand.Intn(100)
	b := rand.Intn(100)
	GCD := Euclid(a, b)
	fmt.Println(a, b)
	fmt.Println(GCD)
	fmt.Println(GCD == (int)(gcd(uint64(a), uint64(b))))
}

func Euclid(a, b int) int {
	x, y := a, b
	if a < b {
		x, y = b, a
	}
	for {
		if x%y == 0 {
			return y
		} else {
			tmp := x % y
			x = y
			y = tmp
		}
	}
}

func gcd(m, n uint64) uint64 {
	x := new(big.Int)
	y := new(big.Int)
	z := new(big.Int)
	a := new(big.Int).SetUint64(m)
	b := new(big.Int).SetUint64(n)
	return z.GCD(x, y, a, b).Uint64()
}
