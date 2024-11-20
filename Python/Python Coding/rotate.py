def rotate(input,d): 
  
    # slice string in two parts for left and right 
    Lfirst = phrase[0 : d] 
    Lsecond = phrase[d :] 
    Rfirst = phrase[0 : len(phrase)-d] 
    Rsecond = phrase[len(phrase)-d : ] 
  
    # now concatenate two parts together 
    print ("Left Rotation : ", (Lsecond + Lfirst) )
    print ("Right Rotation : ", (Rsecond + Rfirst) )
  
  # Driver program 
if __name__ == "__main__": 
    phrase = input("Enter a phrase : ")
    d = int(input("Enter number of rotations "))
   
    rotate(phrase,d) 