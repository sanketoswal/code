def Packet(packet1):
    
    data=packet1&((1<<15)-1)
    packet1=packet1>>15
    len1=packet1&((1<<9)-1)
    packet1=packet1>>9
    flag=packet1&1
    packet1=packet1>>1 
    crc=packet1&((1<<7)-1)
    return data,len1,flag,crc    
    

def main():
    no=eval(input("Enter A number to depack"))
    crc,flag,len1,data=Packet(no)
    print(crc,flag,len1,data)

        

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            
