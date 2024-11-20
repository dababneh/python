#Repeating Letters :

def find_duplicate(sample):
    count = {}
    sample.split()
    
    for n in sample:
        if n in count and count[n] == 2:
            return n, count[n]
        if n not in count:
            count[n] = 1
        elif count[n] == 1:
            count[n]+= 1
            return n, count[n]
        
    return("no duplciates found")




sample = "abcdd"
print(find_duplicate(sample))
