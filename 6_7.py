def MaximumNumber(iData):

    iMax = iData[0]

    for iNo in iData:
        if (iNo > iMax):
            iMax = iNo
    return iMax
    
def main():
    print("Enter numbers : ")
    iValues = []

    for iCnt in range(5):
        element = int(input())
        iValues.append(element)

    iRet = MaximumNumber(iValues)

    print("Maximum number is : ",iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>python 6_7.py
Enter numbers :
23
89
12
56
45
Maximum number is :  89

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_6>

'''