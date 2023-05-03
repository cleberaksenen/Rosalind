# from Bio.Seq import Seq

DNA_set = {"A":"T", "T":"A", "C":"G", "G":"C"}
DNA = "AAAACCCGGT"
comp_DNA = ""
for nuc in DNA:
    comp_DNA = comp_DNA + DNA_set[nuc]

rev_comp_DNA = comp_DNA[::-1]
print(rev_comp_DNA)


