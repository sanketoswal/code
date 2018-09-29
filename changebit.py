def TurnOnBits(no1,no2,pos,bits):
    x=(1<<bits)-1#we created 00001111
    x=x<<(pos-bits)# for position 00011110 in this case we used position 4
    
    no1_part=no1&x #removing that much bits
    no2_part=no2&x #this will be 

    no1=no1&~x #complement of x now we remove bits from no1
    no2=no2&~x #same thing with no2

    no1=no1|no2_part
    no2=no2|no1_part

    return no1,no2
    

def main():
    no1,no2,pos,bits=eval(input("Enter two no  pos and bits"))
    y,x=TurnOnBits(no1,no2,pos,bits)
    print(x,y)

        

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            
