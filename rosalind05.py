with open("rosalind05.fasta", "r") as input:
    fastas = input.readlines()

with open("rosalind05_out.fasta", "w") as output:
    for fasta in fastas:
        if fasta.startswith(">"):
            output.write("\n" + fasta)
        else:
            output.write(fasta.strip("\n"))
    fastas_out = output.readlines()

names = []
sequencia = []
for fasta in fastas_out:
    if fasta.startswith(">"):
        names.append(fasta)
    else:
        sequencia.append(fasta)
print(names)
print(sequencia)









