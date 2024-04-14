#Kyler Pace
def encode(password):
    encoded_password = ''
    for i in password:
        encoded_digit = str((int(i) + 3) % 10)
        encoded_password += encoded_digit
    print("Your password has been encoded and stored!")
    return encoded_password


#Noah Shellenberger
def decoder(password):
    decoded_password =''
    for digit in password:
        decode_digit = str((int(digit)-3) % 10)
        decoded_password += decode_digit
    return decoded_password

def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3.Quit')
        x = int(input('Please enter an option:'))
        if x == 1:
            y = input('Please enter your password to encode:')
            encoded = encode(y)
            print('Your password has been encoded and stored!')
        elif x == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif x==3:
            break

if __name__=='__main__':
    main()
