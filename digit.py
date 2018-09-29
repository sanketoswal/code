def digit(no):
    sum=0
    while(no!=0):
       sum=no%10
       no=int(no/10)
       print(sum)
       return digit(int(no))
 
def main():
    no=eval(input("Enter  A number"))
    digit(no)
    
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
