package main

func productExceptSelf(nums []int) []int {
	n := len(nums)
	res := make([]int, n)

	asc := make([]int, n)
	asc[0] = nums[0]
	for i := 1; i < n; i++ {
		asc[i] = asc[i-1] * nums[i]
	}

	desc := make([]int, n)
	desc[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		desc[i] = desc[i+1] * nums[i]
	}

	res[0] = desc[1]
	res[n-1] = asc[n-2]
	for i := 1; i < n-1; i++ {
		res[i] = asc[i-1] * desc[i+1]
	}

	return res
}
