class ArrayX:
     def __init__(self,size):
         self.size = size
         self.Arr = [0] * size

     def Accept(self):
         print("Enter The Elements : ")

         for i in range(self.size):
             Value = int(input())
             self.Arr[i] = Value

     def Display(self):
         print("Elements of the Arry are : : ")

         for i in range(self.size):
             print(self.Arr[i])


     def Summation(self):
         iSum = 0

         for i in range(self.size):
             iSum = iSum + self.Arr[i]


         return iSum  

     
def main():
     aobj = ArrayX(5)
     aobj.Accept()

     aobj.Display()

     print("Summation is : ",aobj.Summation())
     
     if __name__ == "__main__":
         main()


# numpy libriry
# swatah che swatah try kara 