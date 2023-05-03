# DNA = "GATGGAACTTGACTACGTAAATT"
# print(DNA.replace("T", "U"))

from Bio.Seq import Seq
DNA = Seq("GATGGAACTTGACTACGTAAATT")
RNA = DNA.transcribe()
print(RNA)

