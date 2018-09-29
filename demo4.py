def Pattern(row):
    for i in range(row):
        for _ in range(i):
            print(' \t',end=" ")
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
        
#umake the code generic that means if user enters a :All four
''' a
    aa
    aaa
    aaa
'''
