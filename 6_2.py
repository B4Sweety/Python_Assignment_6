def SumOfEvenNumbers():
    iNo = 1
    iSum = 0
    while(iNo <= 100):
        if((iNo % 2) == 0):
            iSum = iSum + iNo
        iNo = iNo + 1
    return iSum


def main():
    iRet = SumOfEvenNumbers()
    print("Sum of even numbers between 1 to 100 is : ",iRet)

if __name__ == "__main__":
    main()

'''


C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>python 6_2.py
Sum of even numbers between 1 to 100 is :  2550

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>

'''