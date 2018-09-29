def Pattern(row):
    for i in range(1,row+1):
        k=64+i;
        for _ in range(row-i):
            print('\t',end='')
            
        j=0
        for l in range(2*i-1):
            print(chr(k+j)+"\t",end='')
            if l<(i-1):
                j=j-1
            else:
                j=j+1
        print("")
           
    
def main():
    row=eval(input("Enter Number of Rows"))
    Pattern(row)
   

if __name__=='__main__':
    main()
else:
    print("loaded as module",__name__)        
        
#hw
#   1
# 2 1 2
#32 1 2 3


'''
D C B A B C D
  C B A B C
    B A B
      A
'''
