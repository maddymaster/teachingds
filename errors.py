while True:
    try:
        x = int(input("Enter a number: "))
        break
    except (ValueError, KeyboardInterrupt) :
        print('Thats not a valid number')
        break
    finally:
        print("\nAttempted Input\n")
