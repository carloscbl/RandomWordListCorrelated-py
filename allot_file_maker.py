from random import randint , getrandbits
import codecs

def render_matrix(matrix):
    string = ""
    for lista in matrix:
        string += '\n'
        for palabras in lista:
            string += palabras + " "
    return string


def gen_sufix(bananas,word):
    if bananas > 0:
        pass
    else:
        return get_randomWord()

vocales = "aeiou"#AEIOUÀÁÉÈÍÌÒÓÚÙ
consonantes = "bcdfghjklmnpqrstvwxyz" #$€Ç

def get_randomWord():
    pass

def get_randomSilaba():
    silabaSimple = getrandbits(1)
    index = randint(0,len(consonantes)-1)
    index2 = randint(0,len(vocales)-1)
    formacion += consonantes[index] + vocales[index2]
    if not bool(silabaSimple):
        index = randint(0,len(consonantes)-1)
        formacion += consonantes[index]

def genApostrofes(lines):
    matriz = []
    for lineas in range(0, lines):
        lista = []
        for palabras in range(0,randint(1,5)): 
            formacion = ""
            for silabas in range(0,randint(1,4)): 
                
            lista.append(formacion)
        matriz.append(lista)
    return matriz

def addsuffix(matrix):
    for lista in matrix:
        for word in lista:
            word = gen_sufix( rraannddomm int, word )


def main():
    print("Culion")
    total_lines = 512
    listaA = render_matrix(genApostrofes(total_lines))
    #listaB = getrand(total_lines, "Lista B")
    file = codecs.open("lista_allot.txt","w","utf-8-sig")
    file.write(listaA)
    #file.write(listaB)



if __name__ == "__main__":
    main()