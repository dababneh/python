

#class program :
    #def __init__(self, num1) :
        #self.num1 = num1

def func (num1):
        if num1 > "0" :
            print (num1 + " is positiive")
        elif num1 < "0" :
            print (num1 + " is negative")
        else:
            print (num1 + " is zero")
def check (): 
    x = input("\nEnter a number or type stop to abort: ")
    abort = "stop"
    if x == abort :
        print("Program ended")
    else : 
        func (x)
        check ()
    
    
    
        
check()

