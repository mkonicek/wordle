# Helps solve [Wordle](https://www.powerlanguage.co.uk/wordle) and other similar games.
#
# Usage:
#
# python3 wordle.py

from suggestion import suggestion

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

print(f"How about:", ', '.join(suggestion(words, [], allowed, freq)))

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
    print(f"How about:", ', '.join(suggestion(words, possible, allowed, freq)))