def Pattern(row):
    for i in range(row):
        for _ in range(row-i):
            print('*\t',end=" ")
        print(" ")
        
    
           
    
def main():
    row=eval(input("Enter Number of Rows"))
    Pattern(row)
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#use square root for more efficient process
