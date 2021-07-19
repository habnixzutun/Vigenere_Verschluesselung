from tkinter import *
from tkinter import filedialog
import os
import random

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def encrypt(text, schlussel):
    geheimtext = ""
    for i, j in zip(text, schlussel):
        try:
            #print(i)
            temp = i.isupper()
            i = i.upper()
            if i == " ":
                geheimtext += " "
            if i == "\t":
                geheimtext += "\t"
            if i == "\n":
                geheimtext += "\n"
            else:
                try:
                    if temp:
                        geheimtext += abc[abc.index(i) + (abc.index(j))]
                    else:
                        geheimtext += abc[abc.index(i) + (abc.index(j))].lower()
                except IndexError:
                    if temp:
                        geheimtext += abc[(abc.index(i) + (abc.index(j))) - 26]
                    else:
                        geheimtext += abc[(abc.index(i) + (abc.index(j))) - 26].lower()
        except ValueError:
            geheimtext += " "
    return geheimtext


def decrypt(text, schlussel):
    geheimtext = ""
    for i, j in zip(text, schlussel):
        try:
            temp = i.isupper()
            i = i.upper()
            if i == " ":
                geheimtext += " "
            if i == "\t":
                geheimtext += "\t"
            if i == "\n":
                geheimtext += "\n"
            else:
                try:
                    if temp:
                        geheimtext += abc[abc.index(i) - (abc.index(j))]
                    else:
                        geheimtext += abc[abc.index(i) - (abc.index(j))].lower()
                except IndexError:
                    if temp:
                        geheimtext += abc[(abc.index(i) - (abc.index(j))) + 26]
                    else:
                        geheimtext += abc[(abc.index(i) - (abc.index(j))) + 26].lower()
        except ValueError:
            geheimtext += " "
    return geheimtext


def save(text):
    global path
    #print(text)
    *path2, filename = path.split("/")
    *name2, extension = filename.split(".")
    name = ""
    for i in list(name2):
        name += i + "."
    path = ""
    for i in path2:
        path += i + "/"
    os.chdir(str(path))
    with open(name + "new." + extension, "w") as file:
        file.write(str(text))


def generate_key():
    key = ""
    for i in range(40):
        key += random.choice(abc)
    key_entry.delete(0, END)
    key_entry.insert(0, key)



def get_path():
    global path
    path = str(filedialog.askopenfilename())
    filepath_entry.delete(0, END)
    filepath_entry.insert(0, path)


def edit_key(mode):
    key = key_entry.get().replace(" ", "")
    if key != "":
        text = str(open(filepath_entry.get(), "r").read())
        #print(text)
        if len(key) <= len(text):
            temp = len(key)
            i = 0
            while len(key) <= len(text):
                key += key[i]
                i += 1
                if i == temp:
                    i = 0
        if mode == 1:
            save(encrypt(text, key.upper()))
        elif mode == 2:
            save(decrypt(text, key.upper()))


main = Tk()
main.geometry("600x450")
main.title("Vigenére Encryption v1.0")


# Row 1
filepath_label = Label(main, text="Filename:", padx=5, pady=5)
filepath_label.grid(row=0, column=0, sticky="w")
filepath_entry = Entry(main, width=60)
filepath_entry.grid(row=0, column=1, ipady=3)
filepath_button = Button(main, text="Select File", width=20, command=get_path)
filepath_button.grid(row=0, column=2, padx=10)


# Row 2
key_label = Label(main, text="Key:", padx=5, pady=20)
key_label.grid(row=1, column=0, sticky="w")
key_entry = Entry(main, width=60)
key_entry.grid(row=1, column=1, ipady=3)
filepath_button = Button(main, text="Generate random key", width=20, command=generate_key)
filepath_button.grid(row=1, column=2, padx=10)


# Row 3
encrypt_button = Button(main, text="Encrypt", width=20, command=lambda: edit_key(1))
encrypt_button.grid(row=2, column=1, padx=0, sticky="w")
decrypt_button = Button(main, text="Decrypt", width=20, command=lambda: edit_key(2))
decrypt_button.grid(row=2, column=1, sticky="e")

main.mainloop()
