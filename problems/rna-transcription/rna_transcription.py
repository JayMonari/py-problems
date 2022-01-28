rna = {
    "C": "G",
    "G": "C",
    "T": "A",
    "A": "U",
}


def to_rna(dna_strand: str) -> str:
    return "".join([rna[nuc] for nuc in dna_strand])
