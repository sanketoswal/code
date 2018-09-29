def add(a,b):
    if b == 1:
        print(a)
        res=a+b
        return res
    else:
        print(b)
        return add(a,b-1)
result=add(5,20)
print(result)

