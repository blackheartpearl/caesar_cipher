from tkinter import *
from tkinter import messagebox


alphabet = 'abcdefghijklmnopqrstuvwxyz'
ch = len(alphabet)
key = 3
cipher = alphabet[key:] + alphabet[:key]


def encrypt():
    ciphered = ''
    result = ''
    field2.delete(0, END)
    txt = field.get()
    if txt.isnumeric() or not txt:
        messagebox.showinfo('Error!', 'Please, enter a word.')
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
    field2.insert(0, f'{result}')


def decrypt():
    ciphered = ''
    result = ''
    field2.delete(0, END)
    txt = field.get()
    if txt.isnumeric() or not txt:
        messagebox.showinfo('Error!', 'Please, enter a word.')
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
    field2.insert(0, f'{result}')


# GUI windows ----------------------------------------------------------
root = Tk()
root.wm_title('Caesar Cipher')
root.minsize(300, 150)

# Labels ---------------------------------------------------------------
label = Label(root, text='Caesar cipher', font='Helvetica')
label.pack()

Slab = StringVar()
label2 = Label(root, textvariable=Slab)
label2.pack()

txt_label = 'Plain text'
Slab.set(txt_label)

field = Entry(root)
field.pack()
decode_txt = Label(root, text='the encrypted text: ')
decode_txt.pack()
field2 = Entry(root)
field2.pack()

button = Button(root, text='Encrypt', width=10, command=encrypt)
button.pack()
button2 = Button(root, text='Decrypt', width=10, command=decrypt)
button2.pack()


root.mainloop()