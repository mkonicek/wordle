def suggestion_score(word, possible, freq):
    score = 0
    for c in set(word):
        for p in possible:
            if c in p:
              break
        f = freq[c]
        if c in {'a', 'e', 'i', 'o', 'u'}:
            f = f / 2
        score = score + f
    return score

def suggestions(words, possible, allowed, freq):
    suggestion_words = [w for w in words if satisfies_allowed(w, allowed)]
    suggestions = [(w, suggestion_score(w, possible, freq)) for w in suggestion_words]
    suggestions_sorted_with_scores = sorted(suggestions, key=lambda t: t[1], reverse=True)[:10]
    suggestions_sorted = [w for (w, s) in suggestions_sorted_with_scores]
    suggestions_dedup = []
    for i in range(len(suggestions_sorted)):
        is_permutation = False
        for j in range(i):
            if set(suggestions_sorted[j]) == set(suggestions_sorted[i]):
                is_permutation = True
        if not is_permutation:
            suggestions_dedup.append(suggestions_sorted[i])

    return suggestions_dedup[:3]

def satisfies_allowed(word, allowed):
    for i in range(len(word)):
        if word[i] not in allowed[i]:
            return False
    return True  