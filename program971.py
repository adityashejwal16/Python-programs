# Count Capital Cahr


def CountCapital(Brr):
    iCount = 0
    for ch in Brr:
       if(ch >= 65 and ch <= 90):   # Issue Assci Value
          iCount = iCount + 1

    return iCount

def main():
   print("Enter String  : ")
   Arr = input()

   Ret = CountCapital(Arr)

   print("Number of capital Character Are : ",Ret)

main()
