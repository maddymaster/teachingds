def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("That is not an integer")
            continue
        # Add a keyboard interrupt exception
        else:
            print("Oh yes thats an integer, you are learning fast! good!")
            break

        finally:
            print("the finally block got executed")

        print(val)

askint()