def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("DNA Strands must be of equal length!")
    return len([n for i, n in enumerate(strand_a) if n != strand_b[i]])
