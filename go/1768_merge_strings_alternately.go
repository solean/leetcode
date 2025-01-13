package main

func mergeAlternately(word1 string, word2 string) string {
	merged := ""

	shorterStr := word1
	longerStr := word2
	if len(word2) < len(word1) {
		shorterStr = word2
		longerStr = word1
	}

	i := 0
	for i < len(shorterStr) {
		merged = merged + string(word1[i])
		merged = merged + string(word2[i])
		i++
	}

	if len(word1) != len(word2) {
		merged = merged + string(longerStr[i:])
	}

	return merged
}
