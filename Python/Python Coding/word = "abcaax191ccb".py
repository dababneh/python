word = "abcaax191ccb"
duplicate = {}
for i in word:
    if i not in duplicate.keys() and i not in ["1","2","3","4","5","6","7","8","9","0"]:
        duplicate[i]=str(word.count(i))

print(duplicate)

def reverseBits(num):
 
    reverseNum = 0
    shiftIdx = 0
 
    # They will probably just do a for loop 32 times
    while(num):
         
        bit = num & 1
         
        reverseNum |= bit << (31 - shiftIdx)
         
        num >>= 1
        shiftIdx += 1
         
    return reverseNum

