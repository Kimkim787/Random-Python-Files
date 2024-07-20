try:
    divisor = int(input("Enter divisor: "))
    dividend = int(input("Enter dividend: "))
    answer = divisor / dividend
except ZeroDivisionError as e:
    print("Divide number by zero is Unidentified!")
except ValueError as e:
    print("Divide number by character?")
except Exception as e:
    print (e)
finally: #              Executes with our without error good for closing files if possible
    print("End of program")