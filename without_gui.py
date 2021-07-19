abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def verschlusseln(text, schlussel):
    geheimtext = ""
    for i, j in zip(text, schlussel):
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
    return geheimtext


def entschlusseln(text, schlussel):
    geheimtext = ""
    for i, j in zip(text, schlussel):
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
    return geheimtext


while True:
    while True:
        try:
            mode = int(input("Verschlüsseln\t= 1\n"
                             "Entschlüsseln\t= 2\n"
                             "Option: "))
            print()
            break
        except ValueError:
            print()
    text = input("Text:\t\t")
    schlussel = input("Schlüssel:\t").upper()
    if schlussel <= text:
        temp = len(schlussel)
        i = 0
        while len(schlussel) <= len(text):
            schlussel += schlussel[i]
            i += 1
            if i == temp:
                i = 0
    if mode == 1:
        print(verschlusseln(text, schlussel) + "\n")
    elif mode == 2:
        print(entschlusseln(text, schlussel) + "\n")
