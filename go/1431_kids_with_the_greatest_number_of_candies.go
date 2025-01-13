package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
	maxCandies := candies[0]
	for _, value := range candies[1:] {
		if value > maxCandies {
			maxCandies = value
		}
	}

	ans := make([]bool, len(candies))

	for i, value := range candies {
		if value+extraCandies >= maxCandies {
			ans[i] = true
		}
	}

	return ans
}
