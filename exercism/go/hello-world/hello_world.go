package hello

import "fmt"

const testVersion = 2

// HelloWorld
func HelloWorld(name string) string {
	if len(name) > 0 {
		return fmt.Sprintf("Hello, %s!", name)
	} else {
		return "Hello, World!"
	}
}
