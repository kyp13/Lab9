#Kyler Pace


def encode(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = str((int(digit)+3)%10)
        encoded_password+=encoded_digit
    return encoded_password

#Noah Shellenberger
def decoder(password):
    decoded_password=''
    for digit in password:
        decode_digit = str((int(digit)-3)%10)
        decoded_password+=decode_digit
    return decoded_password

def main():
    x = input('Would you like to encode (1) or decode (2)?')
    if x == 1:
        y = input('What would you like to be encoded?')
        encode(y)
    elif x == 2:
        z = input('What would you like to be decoded?')
        decoder(y)

if __name__=='__main__':
    main()
