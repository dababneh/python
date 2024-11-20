

name_dict = {

    "John"  : 30, 
    "Jane"  : 19,
    "Joe"   : 22,
    "April" : 21,
}
name_dict ["Jamil"] = 3
print(name_dict.items())

for i in sorted(name_dict.values()):
    for key in name_dict:
        if name_dict[key] == i:
            print(key,i)
            break
    

#2       

import collections

text = "This is an interview. This interview is being conducted in codePad. The laguage used is Python. specifically Python version 3."
words = text.split()
duplicate = collections.defaultdict(int)
for word in words: 
    duplicate[word] += 1

count = {k : v for 
            k, v in duplicate.items()}

duplicate = {k : v for 
            k, v in duplicate.items() if v>1}

            
print("\nThis is the normal word count\n" +str(count))
print("\nThese are the repeated words with their count. \n" +str(duplicate))


        
        
    
        
        
    