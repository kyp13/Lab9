# Noah Shellenberger

def encoder(password):
    for i in password:
        i = int((i + 3)%10)
    return password

def main():
    x = input('Would you like to encode (1) or decode (2)?')
    if x == '1':
        y = input('What would you like to be encoded?')
        encoder(y)
    elif x == '2':
        z = input('What would you like to be decoded?')
        #decoder(y)

if __name__=='__main__':
    main()