package main

func reverseVowels(s string) string {
	vowels := map[rune]bool{
		'a': true,
		'A': true,
		'e': true,
		'E': true,
		'i': true,
		'I': true,
		'o': true,
		'O': true,
		'u': true,
		'U': true,
	}

	runes := []rune(s)

	i := 0
	j := len(runes) - 1

	for i < j {
		if vowels[runes[i]] && vowels[runes[j]] {
			runes[i], runes[j] = runes[j], runes[i]
			i++
			j--
		} else if vowels[runes[i]] {
			j--
		} else if vowels[runes[j]] {
			i++
		} else {
			i++
			j--
		}
	}

	return string(runes)
}
