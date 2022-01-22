# Helps solve [Wordle](https://www.powerlanguage.co.uk/wordle) and other similar games.
#
# Usage:
#
# python3 wordle.py

from load import character_frequencies, load_words
from possible import find_possible
from suggestion_optimal import suggestion_optimal
from suggestions import suggestions

from word_list import wordle_known_solutions, wordle_allowed_guesses

words = wordle_known_solutions #load_words()
freq = character_frequencies(words)    

allowed = [set(), set(), set(), set(), set()]
must_appear = set()
for i in range(len(allowed)):
    for c in freq.keys():
        allowed[i].add(c)

# suggestion = join(suggestions(words, [], allowed, freq)
suggestion = 'raise'
print(f"How about:", suggestion)

attempt = 0
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
    if len(possible) == 1:
        exit()
    #if attempt == 0:
    #    print("How about: liner")
    #else:
    #print(f"How about:", ', '.join(suggestions(words, possible, allowed, freq)))
    print(f"How about:", suggestion_optimal(words, possible, allowed, must_appear))
    attempt = attempt + 1