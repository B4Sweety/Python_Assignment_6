def Factorial(iNo):
    iCnt = 1
    iResult = 1
    for iCnt in range(1, iNo + 1):
            iResult = iResult * iCnt
    return iResult

def main():
    print("Enter a number : ")
    iValue = int(input())

    iRet = Factorial(iValue)

    print("Factorial of",iValue,"is : ",iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>python 6_4.py
Enter a number :
5
Factorial of 5 is :  120

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>

'''