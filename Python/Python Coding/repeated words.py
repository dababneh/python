

text = "This is an interview. This interview is being conducted in codePad. The laguage used is Python. specifically Python version 3."

count_words = {}

text = text.split()

for t in text:
    if t not in count_words:
        count_words[t] = 1
    else:
         count_words[t] +=1 

for (x,y) in count_words.items():
    if y >1 :
        print(x, ":", y)

