#Kyler Pace

def encode(password):
    encoded_password = ' '
    for i in password:
        encoded_digit = str((int(i) + 3) % 10)
        encoded_password += encoded_digit
    print("Your password has been encoded and stored!")
    return encoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        x = int(input("Please enter an option: "))
        if x == 1:
            y = input("What would you like to be encoded? ")
            encoded = encode(y)
            print(encoded)
        elif x == 3:
            break

if __name__ == "__main__":
    main()


