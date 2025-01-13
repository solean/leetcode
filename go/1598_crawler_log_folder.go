package main

func minOperations(logs []string) int {
	stack := []string{}

	for i := 0; i < len(logs); i++ {
		op := logs[i]

		if op == "./" {
			continue
		} else if op == "../" {
			if len(stack) > 0 {
				stack = stack[:len(stack)-1]
			}
		} else {
			stack = append(stack, op)
		}
	}

	return len(stack)
}
