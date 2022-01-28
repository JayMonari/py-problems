def levenshtein_distance(word1: str, word2: str) -> int:
    small = word1 if len(word1) < len(word2) else word2
    big = word1 if len(word1) >= len(word2) else word2
    even_edits = [x for x in range(len(small) + 1)]
    odd_edits = [_ for _ in range(len(small) + 1)]
    for row in range(1, len(big) + 1):
        if row % 2 == 1:
            current_edits = odd_edits
            previous_edits = even_edits
        else:
            current_edits = even_edits
            previous_edits = odd_edits
        current_edits[0] = row
        for col in range(1, len(small) + 1):
            if big[row - 1] == small[col - 1]:
                current_edits[col] = previous_edits[col - 1]
            else:
                current_edits[col] = 1 + min(current_edits[col - 1],
                                             previous_edits[col],
                                             previous_edits[col - 1])

    return even_edits[-1] if len(big) % 2 == 0 else odd_edits[-1]


print(levenshtein_distance("abc", "abbb"))
