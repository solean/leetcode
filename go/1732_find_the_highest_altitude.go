package main

func largestAltitude(gain []int) int {
	maxAltitude := gain[0]

	ps := make([]int, len(gain))
	ps[0] = gain[0]

	for i := 1; i < len(gain); i++ {
		ps[i] = ps[i-1] + gain[i]
		maxAltitude = max(maxAltitude, ps[i])
	}

	return max(0, maxAltitude)
}
