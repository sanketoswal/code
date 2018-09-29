def main():
    x=eval(input("How many numbers do u want to enter"))
    our_list = [] 
    for i in range(0, x):
        number=eval(input("Enter number"))
        our_list.append(number)
    for j in range(0,x):
        if(our_list[j]&1):
            print("{} The number is odd".format(our_list[j]))
        else:
            print("{} The Number is Even".format(our_list[j]))

        

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            
