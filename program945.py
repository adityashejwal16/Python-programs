# Even Odd Number

def CheckEven(No):
     if(No % 2 == 0):
         print("It is Even Number")
     else:
         print("it is odd number")

def main():
    Value = 0

    print("Enter Number : ")
    Value = int(input())

    CheckEven(Value)

main()
