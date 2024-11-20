import re

phrase = "A man, a Plan, a canal: Panama"


def check_palaindrome(phrase : str) -> str:
    if not phrase:
        return "Phrase is empty"
    
    phrase = [x for x in phrase if x.isalpha()]
    phrase = "".join(phrase)
    phrase = phrase.lower()
    print(phrase)

    if phrase == phrase[::-1]:
        return "Yes the phrase is plaindrome or whatever"
    else:
        return "Phrase is weird and not plaindrome"

print(check_palaindrome(phrase))