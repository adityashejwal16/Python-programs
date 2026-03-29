# Count Capital Cahr


def CountCapital(Brr):
    iCount = 0
    for ch in Brr:
       if(ord(ch) >= 65 and ord(ch) <= 90):   # Ascii Value get in ord
          iCount = iCount + 1

    return iCount

def main():
   print("Enter String  : ")
   Arr = input()

   Ret = CountCapital(Arr)

   print("Number of capital Character Are : ",Ret)

main()
