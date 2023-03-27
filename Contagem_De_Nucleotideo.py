""" Algoritmos em Bioinformática
    Bruno Batista Lescher
    Contagem da sequência de DNA"""

sequenciaDNA = input('Insira a sequência de DNA: ')

ADNA = int
TDNA = int
GDNA = int
CDNA = int

ADNA = sequenciaDNA.count('A') 
TDNA = sequenciaDNA.count('T')
GDNA = sequenciaDNA.count('G')
CDNA = sequenciaDNA.count('C')

print(f'\nA sequência de DNA inserida possui:\n\nAdenina (A): {ADNA} \nGuanina (G): {GDNA} \nCitosina (C): {CDNA}\nTimina (T): {TDNA}')

print('\nTotal de nucleotídeos na sequência de DNA: {}'.format(ADNA + GDNA + CDNA + TDNA))

