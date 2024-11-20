def is_palindrome(input_string):
# We'll create two strings, to compare them
	new_string = input_string.replace(" ", "").lower()
	reverse_string = input_string.replace(" ",""). lower()[::-1]
	if new_string == reverse_string:
		return True
	return False