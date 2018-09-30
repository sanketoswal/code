def main():
    
    x=eval(input("How many numbers do u want to enter in list 1"))
    l1 = [] 
    for i in range(0, x):
        number=eval(input("Enter number"))
        l1.append(number)
    for i in range (0,x):
        print(type(l1[i]))
        
    print(l1)

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            

''' OUTPUT
How many numbers do u want to enter in list 14
Enter number[1,2]
Enter number2
Enter number3
Enter number"hello"
<class 'list'>
<class 'int'>
<class 'int'>
<class 'str'>
[[1, 2], 2, 3, 'hello']'''
