package main

import (
	"strings"
)

func gcdOfStrings(str1 string, str2 string) string {
	smallerStr := str1
	if len(str2) < len(str1) {
		smallerStr = str2
	}

	for i := len(smallerStr); i >= 1; i-- {
		if len(str1)%i == 0 && len(str2)%i == 0 {
			div := smallerStr[:i]
			if str1 == strings.Repeat(div, len(str1)/i) && str2 == strings.Repeat(div, len(str2)/i) {
				return div
			}
		}
	}

	return ""
}
