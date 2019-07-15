from random import randint , getrandbits
import codecs

vocales = "aeiou"#AEIOUÀÁÉÈÍÌÒÓÚÙ
consonantes = "bcdfghjklmnpqrstvwxyz" #$€Ç

def render_matrix(matrix):
    string = ""
    for lista in matrix:
        string += '\n'
        for palabras in lista:
            string += palabras + " "
    return string

def gen_sufix(bananas,word):
    if bananas > 0:
        suffixed = word
        for i in range(0,bananas):
            suffixed = get_randomSilaba(suffixed)
        return suffixed
    else:
        return get_randomWord()

def get_randomWord():
    formacion = ""
    for silabas in range(0,randint(1,4)): 
        formacion = get_randomSilaba(formacion)
    return formacion
    
def get_randomSilaba(composition):
    silabaSimple = getrandbits(1)
    index = randint(0,len(consonantes)-1)
    index2 = randint(0,len(vocales)-1)
    composition += consonantes[index] + vocales[index2]
    if not bool(silabaSimple):
        index = randint(0,len(consonantes)-1)
        composition += consonantes[index]
    return composition

def genApostrofes(lines):
    matriz = []
    for lineas in range(0, lines):
        lista = []
        for palabras in range(0,randint(1,5)): 
            lista.append(get_randomWord())
        matriz.append(lista)
    return matriz

def addsuffix(matrix):
    matrix2 = []
    for lista in matrix:
        list2 = []
        for word in lista:
            list2.append( gen_sufix( randint(0,3), word ))
        matrix2.append(list2)
    return matrix2

def main():
    print("Culion")
    total_lines = 512
    matrix = genApostrofes(total_lines)
    listaA = render_matrix(matrix)
    #listaB = getrand(total_lines, "Lista B")
    file = codecs.open("lista_allot.txt","w","utf-8-sig")
    file.write(listaA)
    file = codecs.open("lista_allot2.txt","w","utf-8-sig")
    listaB = render_matrix(addsuffix(matrix))
    file.write(listaB)

if __name__ == "__main__":
    main()