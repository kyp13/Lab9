# Noah Shellenberger

def encoder(password):
    for i in password:
        i = int((i + 3)%10)
    return password

#Kyler Pace

def decoder(password):
    decoded_password =''
    for digit in password:
        decode_digit = str((int(digit)-3) % 10)
        decoded_password += decode_digit
    return decoded_password

def main():
    while True:
        x = input('Would you like to encode (1) or decode (2)?')
        if x == '1':
            y = input('What would you like to be encoded?')
            encoder(y)
            print('Your password has been encoded and stored!')
        elif x == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif x == 3:
            break

if __name__=='__main__':
    main()