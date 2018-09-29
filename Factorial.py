def factorial(no):
    fact=2
    sum=0
    if(fact!=no):
        sum=sum*fact
        fact+=1
        
    else:
        return sum
        
    
           
    
def main():
    no=eval(input("Enter  A number"))
    x=factorial(no)
    print(x)
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
