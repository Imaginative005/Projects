# dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

file = open(r"C:\Users\Techi\OneDrive\Desktop\rosalind_dna.txt", mode="r")
dna = file.readline()
print(dna)


def condn(dna_string):
    for codn in dna_string:
        if codn == "A":
            a = dna_string.count("A")
        elif codn == "C":
            c = dna_string.count("C")

        elif codn == "G":
            g = dna_string.count("G")
        elif codn == "T":
            t = dna_string.count("T")
    return f'{a} {c} {g} {t}'

print(condn(dna))
