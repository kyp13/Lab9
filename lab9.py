# Noah Shellenberger
def encoder(password):
    encoded_password = ''
    for digit in password:
        encode_digit = str((int(digit)+3)%10)
        encoded_password +=encode_digit
    return encoded_password