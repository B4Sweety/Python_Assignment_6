def CheckPrime(iNo):
    if (iNo <= 1):
        for iCnt in range(2, iNo):
            if((iNo % iCnt) == 0):
                return False
            else:
                return True
    else:
        return False

def main():
    print("Enter a number : ")
    iValue = int(input())

    bRet = CheckPrime(iValue)

    if(bRet == True):
        print(iValue,"is a prime number")
    else:
        print(iValue,"is not a prime number")

if __name__ == "__main__":
    main()