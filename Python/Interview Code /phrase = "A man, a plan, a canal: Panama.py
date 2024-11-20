phrase = "A man, a plan, a canal: Panama"

def palindrome(phrase):
    phrase = phrase.lower()
    phrase = "".join([x for x in phrase if x.isalpha()])
    if phrase == phrase[::-1]:
        return print("yes")
    else:
        return print("no")


palindrome(phrase)


phrase1 = "A man, a plan, a canal: Panama"

phrase1 = phrase1.lower()
phrase1 = "".join(x for x in phrase1 if x.isalpha())

if phrase1 == phrase1[::-1]:
    print("Yes")

else:
    print("No")