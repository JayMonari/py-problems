def convert(n: int) -> str:
    noises = f"{'' if n % 3 else 'Pling'}{'' if n % 5 else 'Plang'}{'' if n % 7 else 'Plong'}"
    return noises if noises else f"{n}"
