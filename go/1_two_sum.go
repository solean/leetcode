package main

func twoSum(nums []int, target int) []int {
	valueMap := make(map[int]int)

	for index, value := range nums {
		complementIndex, exists := valueMap[target-value]
		if exists {
			return []int{complementIndex, index}
		} else {
			valueMap[value] = index
		}
	}

	return nil
}
