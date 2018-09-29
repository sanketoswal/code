def factorial(no):
    if no<0:
        return "Dosent exist"
    elif no==0 or no==1:
        return 1
    else:
        fact=1
        for x in range(2,no+1):
            fact=fact+x
    return fact
        
    
def main():
    no=eval(input("Enter  A number"))
    print("Factorial of {1} is {0}".format(factorial(no),no))
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
