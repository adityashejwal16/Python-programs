# List[]
# Same As Array



def main():
    Size = 0
    Arr = []

    print("Enter Number of Element : ")
    Size = int(input())

    print("Enter the Elements : ")

    value = 0

    for i in range(Size):
        value = int(input())
        Arr.append(value)

    print(Arr)    

main()
