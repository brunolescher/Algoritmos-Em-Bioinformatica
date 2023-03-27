from Bio import SeqIO
import math
import matplotlib.pyplot as plt

def process_fasta_file(filename):
    nucleotide_counts = {}  # inicializa um dicionário vazio para armazenar a contagem de nucleotídeos de cada sequência
    gc_percentages = []     # inicializa uma lista vazia para armazenar as porcentagens de GC de cada sequência
    melting_temps = []      # inicializa uma lista vazia para armazenar as temperaturas de anelamento de cada sequência

    with open(filename, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            seq = str(record.seq)                     # extrai a sequência de nucleotídeos como uma string
            counts = {'A': seq.count('A'), 'T': seq.count('T'), 'G': seq.count('G'), 'C': seq.count('C')}   # conta o número de cada nucleotídeo na sequência
            nucleotide_counts[record.id] = counts     # adiciona a contagem de nucleotídeos ao dicionário
            total_bases = sum(counts.values())        # calcula o número total de nucleotídeos na sequência
            total_gc = counts['G'] + counts['C']      # calcula o número total de nucleotídeos G e C na sequência
            gc_percent = total_gc / total_bases * 100 # calcula a porcentagem de GC na sequência
            melting_temp = 64.9 + 41 * (total_gc - 16.4) / total_bases # calcula a temperatura de anelamento da sequência

            gc_percentages.append(gc_percent)         # adiciona a porcentagem de GC à lista gc_percentages
            melting_temps.append(melting_temp)        # adiciona a temperatura de anelamento à lista melting_temps

            # Imprime os resultados para cada sequência
            print(f"Sequência: {record.id}")
            print(f"A: {counts['A']}, T: {counts['T']}, G: {counts['G']}, C: {counts['C']}")
            print(f"Total de Nucleotídeos na Sequência: {counts['A']+counts['T']+counts['G']+counts['C']}")
            print(f"Porcentagem GC: {gc_percent:.2f}%")
            print(f"Temperatura Melting: {melting_temp:.2f}°C\n")

    # plota os dados em um gráfico de dispersão
    plt.scatter(gc_percentages, melting_temps)
    plt.xlabel('Porcentagem GC')
    plt.ylabel('Temperatura de Anelamento (°C)')
    plt.title('Gráfico de Porcentagem GC versus Temperatura de Anelamento')
    plt.show()

filename = "Influenza H3N2.fasta"
process_fasta_file(filename)
