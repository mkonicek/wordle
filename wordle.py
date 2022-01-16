# Helps solve [Wordle](https://www.powerlanguage.co.uk/wordle) and other similar games.
#
# Usage:
#
# python3 wordle.py

def load_words():
    words = []
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    return words

def character_frequencies(words):
    freq = {}
    for word in words:
        for char in word:
            if char in freq:
                freq[char] = freq[char] + 1
            else:
                freq[char] = 1
    return freq

words = load_words()
freq = character_frequencies(words)    

allowed = [set(), set(), set(), set(), set()]
must_appear = set()
for i in range(len(allowed)):
    for c in freq.keys():
        allowed[i].add(c)

def suggestion_score(word, possible):
    score = 0
    for c in set(word):
        for p in possible:
            if c in p:
              break
        f = freq[c]
        if c in {'a', 'e', 'i', 'o', 'u'}:
            f = f / 3
        score = score + f
    return score

def suggestion(words, possible):
    suggestions = [(w, suggestion_score(w, possible)) for w in words]
    suggestions_sorted_with_scores = sorted(suggestions, key=lambda t: t[1], reverse=True)[:50]
    suggestions_sorted = [w for (w, s) in suggestions_sorted_with_scores]
    suggestions_dedup = []
    for i in range(len(suggestions_sorted)):
        is_permutation = False
        for j in range(i):
            if set(suggestions_sorted[j]) == set(suggestions_sorted[i]):
                is_permutation = True
        if not is_permutation:
            suggestions_dedup.append(suggestions_sorted[i])

    return suggestions_dedup[:10]

def is_possible(word, allowed, must_appear):
    for i in range(len(word)):
        if word[i] not in allowed[i]:
            return False
    for m in must_appear:
        if m not in word:
            return False
    return True

def find_possible(words, allowed, must_appear):
    return [word for word in words if is_possible(word, allowed, must_appear)]

print(f"How about:", ', '.join(suggestion(words, [])))

while True:
    guess = input("What word did you guess? ")
    for i in range(len(guess)):
        g_char = guess[i]
        res = input(f"What was the colour of character {g_char} (b, y, g)? ")

        if res == 'b':
            for j in range(len(guess)):
                if g_char in allowed[j]:
                    allowed[j].remove(g_char)

        if res == 'y':
            # The yellow character must appear in the word
            must_appear.add(g_char)
            # But the yellow character cannot be at that position
            if g_char in allowed[i]:
                allowed[i].remove(g_char)
                  
        if res == 'g':
            allowed[i] = { g_char }

    possible = find_possible(words, allowed, must_appear)

    print(f"OK, there are now {len(possible)} possible words:", ', '. join(possible))
    print(f"How about:", ', '.join(suggestion(possible, possible)))