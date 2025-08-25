#!/bin/Python

print("Paix et Salut de Dieu sur notre bien aimé \u2764")
print("")
# Ce programme permet de demander un verbe(regulier) a l'utiluseur, et le conjuguer au temps simple i.A

def present(verbe):
    racine = verbe[:-2]
    pronom = ['Je','Tu','Il/Elle/on','Nous','Vous','Ils/Elles']
    terminaison = ['e','es','e','ons','ez','ent']
    conjugaison = [f"{pronom}{racine}{terminaison}" for pronom, term in zip(pronom,terminaison)]
    return conjugaison
def conjuguer_verbe():
    verbe = input("Entrer un verbe du premier groupe à l'infinitif : ").strip()
    if verbe.endswith('er'):
        print("\n".join(present(verbe)))
    else:
        print("Ce programme ne gère pas pour le moment ce type de verbe !!!")
if __name__ == "__name__":
    conjuguer_verbe()
print("")
print("Paix et Salut de Dieu sur notre bien aimé \u2764")