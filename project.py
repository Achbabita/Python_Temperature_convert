def get_user_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def cel_fah():
    C=float(input("Enter the celsius degree to convert into Fahrenheit:"))
    F = (C * 9/5) + 32
    print("Fahrenheit degree:",F)
    print("         ")


def cel_kel():
    C=float(input("Enter the celsius degree to convert into Kelvin:"))
    K = C + 273.15
    print("Kelvin degree:",K)
    print("         ")
    

def fah_cel():
    F=float(input("Enter the Fahrenheit degree to convert into celsius:"))
    C = (F-32)* 5/9
    print("Fahrenheit:",C)
    print("         ")


def fah_kel():
    F=float(input("Enter the Fahrenheit degree to convert into Kelvin:"))
    K = (F - 32) * 5/9 + 273.15
    print("Kelvin degree:",K)
    print("         ")

def kel_fah():
        K=float(input("Enter the Fahrenheit degree to convert into Kelvin:"))
        F = (K - 273.15) * 9/5 + 32
        print("Fahrenheit degree:",F)
        print("     ")

def kel_cel():
    K=float(input("Enter the kelvin degree to convert into celsius:"))
    C = K - 273.15
    print("Celsius degree:",C)
    print("         ")



while True:
    print("--Welcome to the temperature converter program--")
    print("1.celsius to fahrenheit\n2.celsius to kelvin\n3. fahrenheit to kelvin\n4.fahrenheit to celsius\n5.kelvin to fahrenheit\n6.kelvin to celsius\n7.Exit")
    print("         ")
    try:
        choice =int(input("Enter your choice(1/2/3/4/5/6/7):"))
    except ValueError:
        print("Invalid input, enter an integer between 1 and 7.")
        continue

    if choice==1:
        cel_fah()
    elif choice==2:
        cel_kel()
    elif choice==3:
        fah_kel()
    elif choice==4:
        fah_cel()
    elif choice==5:
        kel_fah()
    elif choice==6:
        kel_cel()
    elif choice==7:
        break
    else:
        print("Please provide valid input!!!")
   