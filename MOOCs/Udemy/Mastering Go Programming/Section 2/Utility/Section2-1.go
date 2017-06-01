package Utility

import "fmt"

// SayHello is to say howdy
func SayHello() {
	fmt.Println("Hello!!")
}

func Say(s string, i int) {
	fmt.Println(s, i)
}

func addSubtractMultiply(a, b int) (addition, subtraction, multiplication int) {
	addition = a + b
	subtraction = a - b
	multiplication = a * b
	return
}
