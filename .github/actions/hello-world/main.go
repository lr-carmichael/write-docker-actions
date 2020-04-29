package main

import (
	"fmt"
	"os"
)

func main() {

	// Access Inputs as environment variables
	firstGreeting := os.Getenv("INPUT_FIRSTGREETING")
	secondGreeting := os.Getenv("INPUT_SECONDGREETING")
	thirdGreeting := os.Getenv("INPUT_THIRDGREETING")

	// Use those inputs in the actions logic
	fmt.Println("Hello " + firstGreeting)
	fmt.Println("Hello " + secondGreeting)

	// Sometimes inputs are not required...
	if thirdGreeting != "" {
		fmt.Println("Hello " + thirdGreeting)
	}

}
