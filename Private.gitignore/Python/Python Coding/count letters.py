

def count_letters(phrase):
    count = {}
    for i in phrase:
        if i is not " ":
            if i in count:
                 count[i]+=1
            else:
                count[i] = 1
    return count


print(count_letters("Jamil is amazing"))