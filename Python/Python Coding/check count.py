
string = "BBEEEEECCCCDDDDDDDDDDDBBB"

def check_count(string):
    count = {}

    for i in string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        
    
print(check_count(string))