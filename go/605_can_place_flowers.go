package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	count := 0

	for i, val := range flowerbed {
		if val == 1 {
			continue
		}

		if (i == 0 || flowerbed[i-1] == 0) &&
			(i == len(flowerbed)-1 || flowerbed[i+1] == 0) {

			count += 1
			flowerbed[i] = 1
		}
	}

	return count >= n
}
