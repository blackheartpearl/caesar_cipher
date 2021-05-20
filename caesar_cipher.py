alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
ch = len(alphabet)
cipher = alphabet[key:] + alphabet[:key]


def head(txt):
    print('=-' * 10)
    print(txt.center(20))
    print('=-' * 10)


def menuL():
    head('Caesar Cipher')
    opc = readInt('''
[1] Encrypt 
[2] Decrypt 
[3] Quit

your option: ''')
    return opc

# function to read a value and return an error if integer value is not typed
def readInt(opc):
    while True:
        try:
            enter = int(input(opc))
        except (ValueError, TypeError):
            print('\033[31mERROR: type an integer value!\033[m')
        else:
            return enter


# function to encrypt the message------------------------------------------
def encrypt():
    ciphered = ''
    result = ''
    txt = str(input('Enter the text to encrypt: '))
    for i in range(len(txt)):
        for x in range(ch):
            if txt[i].lower() == alphabet[x]:
                ciphered += cipher[x]

    dict_cipher = [x for x in ciphered]
    for x in range(len(txt)):
        if txt[x] == ' ':
            dict_cipher.insert(x, ' ')
    for i in dict_cipher:
        result += i
    print(f'the encrypted message is \033[34m{result}\033[m')


# function to decrypt the message ------------------------------------------
def decrypt():
    ciphered = ''
    result = ''
    txt = str(input('Enter the text to decrypt: '))
    for i in range(len(txt)):
        for x in range(len(cipher)):
            if txt[i].lower() == cipher[x]:
                ciphered += alphabet[x]

    dict_cipher = [x for x in ciphered]
    for x in range(len(txt)):
        if txt[x] == ' ':
            dict_cipher.insert(x, ' ')
    for i in dict_cipher:
        result += i
    print(f'the decrypted message is: \033[34m{result}\033[m')


# main program -----------------------------------------------
while True:
    ans = menuL()
    if ans == 1:
        encrypt()
    elif ans == 2:
        decrypt()
    elif ans == 3:
        head('See you soon!')
        break
    else:
        print('\033[31mERROR! Type a valid option\033[m')