#Reverse word


def reverse_word(words):
    words = words.split()
    print(words[::-1])

words = "Jamil   is      wow "
reverse_word(words)