package g_9_palindrome_number

func isPalindrome(x int) bool {
	n := x
	r := 0
	for n > 0 {
		r = r*10 + n%10
		n /= 10
	}
	return x == r
}
