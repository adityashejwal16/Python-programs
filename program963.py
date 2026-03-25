# List[]
# Same As Array

def Manimum(Brr):
    iMin = Brr[0]

    for i in range(len(Brr)):
        if(Brr[i] > iMin):
            iMin = Brr[i]

    return iMin        

def main():
    Size = 0
    Arr = []

    print("Enter Number of Element : ")
    Size = int(input())

    print("Enter the Elements : ")

    Value = 0

    for i in range(Size):
        Value = int(input())
        Arr.append(Value)

    Ret = Manimum(Arr)    

    print(" Manimum is : ",Ret)

main()
