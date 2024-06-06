alfabeto = "abcdefghijklmnopqrstuvxz"
vogal_prox = "aaaeeeeiiiiiioooooouuuuu"
cons_seg = alfabeto[1:].replace('e','f').replace('i','j').replace('o','p').replace('u','v') + 'z'

vogais = "aeiou"
palavra = input()

for letra in palavra:
    if not(letra in vogais):
        posic = alfabeto.find(letra)
        palavra = palavra.replace(letra, letra + vogal_prox[posic] + cons_seg[posic])
print(palavra)
