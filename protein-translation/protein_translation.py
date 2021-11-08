from typing import Dict, List

translation_table: Dict[str, str] = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}


def proteins(strand: str) -> List[str]:
    translated_proteins: List[str] = []
    codons = [strand[c:c+3] for c in range(0, len(strand), 3)]
    for codon in codons:
        protein = translation_table[codon]
        if protein == "STOP":
            break
        translated_proteins.append(protein)
    return translated_proteins
