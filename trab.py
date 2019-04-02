#encoding: utf-8

QuantAulas = int(input('Quantas aulas tem a disciplina?\n'))
LimiteFaltas =  QuantAulas - int(QuantAulas * 0.75)

print('Limite de faltas na disciplina: ' + str(LimiteFaltas))
print('____________________________________________________________________________')
Faltas = int(input('Digite a quantidade de faltas do aluno?\n'))
print('____________________________________________________________________________')
NotaP1 = float(input('Digite a Nota da P1?\n').replace(",","."))
Ma1 = float(input('Digite a Nota Ma1? \n').replace(",","."))
Mb1 = float(input('Digite a Nota Mb1? \n').replace(",","."))

N1 = ((NotaP1 * 0.7) + (Ma1 * 0.2) + (Mb1 * 0.1))
print('Nota N1 = {:.2f}'.format(N1))
print('____________________________________________________________________________')
NotaP2 = float(input('Digite a Nota da P2 \n').replace(",","."))
Ma2 = float(input('Digite a Nota Ma2 \n').replace(",","."))
Mb2 = float(input('Digite a Nota Mb2 \n').replace(",","."))

N2 = ((NotaP2 * 0.7) + (Ma2 * 0.2) + (Mb2 * 0.1))
print('Nota N2 = {:.2f}'.format(N2))
print('____________________________________________________________________________')

Media = (N1 + (N2 * 2)) / 3

print('A Média do aluno é:  {:.2f}'.format(Media))
print('____________________________________________________________________________')


if Media < 3 and Faltas > LimiteFaltas:
    print('Aluno ficou de DP por nota e faltas! ')
elif Media < 3 and Faltas<= LimiteFaltas:
    print('Aluno ficou de DP por nota')
elif 5 > Media >= 3 and Faltas <= LimiteFaltas and Media < 5:
    print('Aluno fará avaliação RE! ')
elif 5 > Media >= 3 and Faltas > LimiteFaltas:
    print('Aluno ficou de DP por faltas')
elif Media >= 5 and Faltas <= LimiteFaltas:
    print('Aluno Aprovado! ')
elif Media >=5 and Faltas > LimiteFaltas:
    print('Aluno ficou de DP por faltas')
