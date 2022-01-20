# Simulate games of Wordle and evaluate performance of the solver

from load import character_frequencies, load_words
from possible import find_possible, try_guess
from suggestion_optimal import suggestion_optimal
from suggestions import suggestions
import random

random.seed(2003)

MAX_ATTEMPTS = 6
# Not solving is bad. Make it contribute more to the average.
NOT_SOLVED_PENALTY = 10

words = load_words()
freq = character_frequencies(words)

def play_wordle(hidden_word):
    allowed = [set(), set(), set(), set(), set()]
    must_appear = set()
    for i in range(len(allowed)):
        for c in freq.keys():
            allowed[i].add(c)
            
    #guess = suggestions(words, [], allowed, freq)[0]
    guess = 'raise'
    for attempt in range(MAX_ATTEMPTS):
        #if attempt == 1:
        #    guess = 'liner'
        res = try_guess(guess, hidden_word)

        if res == 'g' * len(guess):
            # Solved in this many attempts
            return attempt + 1

        for i in range(len(guess)):
            g_char = guess[i]
            ans = res[i]

            if ans == 'b':
                for j in range(len(guess)):
                    if g_char in allowed[j]:
                        allowed[j].remove(g_char)

            if ans == 'y':
                # The yellow character must appear in the word
                must_appear.add(g_char)
                # But the yellow character cannot be at that position
                if g_char in allowed[i]:
                    allowed[i].remove(g_char)
                    
            if ans == 'g':
                allowed[i] = { g_char }

        possible = find_possible(words, allowed, must_appear)
        guess = suggestion_optimal(words, possible, allowed, must_appear) # Too slow :(

    return NOT_SOLVED_PENALTY

stats = {}

def print_stats(stats):
    print("Statistics:")
    weighted_sum = 0
    total_count = 0
    for attempts in range(MAX_ATTEMPTS + 1):
        count = stats.get(attempts)
        if count != None:
            print(f"{attempts} attemps: {count}")
            weighted_sum = weighted_sum + attempts * count
            total_count = total_count + count       
    did_not_solve = stats.get(NOT_SOLVED_PENALTY)
    if not did_not_solve:
        did_not_solve = 0
    weighted_sum = weighted_sum + NOT_SOLVED_PENALTY * did_not_solve
    total_count = total_count + did_not_solve  
    print(f"Played {total_count} games of Wordle.")     
    print(f"Unsolved Wordles: {did_not_solve}")
    print(f"Solved {(((total_count - did_not_solve) / total_count) * 100):.2f}%")
    print(f"Average attempts: {weighted_sum / total_count:.3f}")    

print(f"Simulating {len(words)} games of Wordle..")
for i in range(3500, len(words)):
    word = words[i]
    attempts = play_wordle(word)
    if attempts not in stats:
        stats[attempts] = 1
    else:
        stats[attempts] = stats[attempts] + 1

    # Print progress
    if (i + 1) % 10 == 0:
        print(f"Played {i + 1} games of Wordle..")

print_stats(stats)