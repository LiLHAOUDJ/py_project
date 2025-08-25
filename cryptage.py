from hashlib import sha256

print("Paix et Salut de Dieu sur notre bien aimé !")
print("")
enter = input("Saisir votre fichier a chiffrer : ")
exit = input("Entrer votre fichier final : ")
cle = input("Entrer votre cle : ")

cles = sha256(cle.encode('utf-8')).digest()
with open(enter, 'rb') as f_enter:
    with open(exit, 'wb') as f_exit:
        i = 0
        while f_enter.peek():
            c = ord(f_enter.read(1))
            j = i % len(cles)
            b = bytes([c^cles[j]])
            f_exit.write(b)
            i = i + 1