def Pattern(row):
    j=65;
    for i in range(1,row+1):
        for k in range(i):
            print(chr(j+k)+'\t',end=" ")
        print(" ")
        
           
    
def main():
    row=eval(input("Enter Number of Rows"))
    Pattern(row)
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
