def DisplayTable(iNo):
    iResult = 0
    for iCnt in range(1,11):
        iResult = iNo * iCnt
        print(iNo,"*",iCnt,"=",iResult)

def main():
    print("Enter number : ")
    iValue = int(input())

    DisplayTable(iValue)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>python 6_3.py
Enter number :
7
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>

'''