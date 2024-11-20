a = ["Wifi", "bT", "cellular", "wiFi", "Bt", "CELLULAR", "A2DP"]


temp = [] 
out = []  

for phrase in a:
    lower_case_phrase = phrase.lower()
    if lower_case_phrase not in temp:
        temp.append(lower_case_phrase)  
        out.append(phrase)

print(out)
