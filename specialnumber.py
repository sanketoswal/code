def SpecialNumber(no):
    
    sum1=0
    temp=no
    if(no<0):
        print("Strong Number Cannot Be Negative")
    while(no!=0):
        i=1
        fact=1
        r=no%10
        while(i<=r):
            fact=fact*i
            i=i+1
        sum1=sum1+fact
        no=(int)(no/10)
    if(sum1==temp):
        print("The number is a strong number")
    else:
        print("The number is not a strong number")
def main():
    no=eval(input("Enter  A number"))
    SpecialNumber(no)
    
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)   
