def Packet(crc,flag,len1,data):
    packet1=crc&127
    packet1=packet1<<1
    packet1=packet1|(flag&1)
    packet1=packet1<<9
    packet1=packet1|(len1&511)
    packet1=packet1<<15
    packet1=packet1|(data&((1<<15)-1))
    return packet1
    
    
    

def main():
    crc,flag,len1,data=eval(input("Enter crc flag len data"))
    x=Packet(crc,flag,len1,data)
    print(x)

        

if __name__=="__main__":
    main()
else:
    print("Loaded as module",__name__)
            
