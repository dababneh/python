myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' : 3, 'manjeet' : 4} 
  
# printing original list 
print("The original dictionary : " + str(test_dict)) 
  
# Using dict() 
# Extracting specifix keys from dictionary 
res = dict((k, test_dict[k]) for k in ['nikhil', 'akshat'] 
                                        if k in test_dict) 
  
# print result 
print("The filtered dictionary is : " + str(res))