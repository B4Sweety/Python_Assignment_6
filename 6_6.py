def DisplayPatter(iNo):

    for i in range(iNo):
        for j in range(iNo):
            if(i >= j):
                print("*",end=" ")
        print()            

def main():
    print("Enter number : ")
    iValue = int(input())

    DisplayPatter(iValue)

if __name__ == "__main__":
    main()