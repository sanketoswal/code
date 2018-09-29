def TurnOnBits(no,pos,bits):
    x=(1<<bits)-1
    x=x<<(pos-bits)
    
    return no|x

def main():
    no,pos,bits=eval(input("Enter no  pos and bits"))
    x=TurnOnBits(no,pos,bits)
    print(x)

        

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            
