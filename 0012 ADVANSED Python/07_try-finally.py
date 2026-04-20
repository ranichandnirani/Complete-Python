# Python offers a ‘finally’ clause which ensures execution of a piece of code inspective of the exception.

def main():
    try:
        a = int(input("Hey, Enter the number: "))
        print(a)
        return


    except Exception as e:
        print(e)
        return

    finally:
        print("Inside finally")
main()