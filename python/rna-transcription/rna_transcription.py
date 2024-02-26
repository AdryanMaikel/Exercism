def to_rna(dna_strand: str) -> str:
    rna = []
    for letter in dna_strand:
        match letter:
            case "G":
                rna.append("C")
            case "C":
                rna.append("G")
            case "T":
                rna.append("A")
            case "A":
                rna.append("U")
            case _:
                rna.append(letter)
    return "".join(rna)
