def isPrime(no):
    if(no<2):
        return False
    elif no==2 or no==3:
        return True
    elif no%2==0:
        return False
    else:
        for x in range(3,int(no/2)+2,2):
            if no%x==0:
                return False
        else:
            return True
    
def main():
    no=eval(input("Enter  A number"))
    if(isPrime(no)):
        print("{} is prime".format(no))
    else:
        print("{} is not prime".format(no))

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
