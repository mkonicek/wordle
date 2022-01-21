import copy
from possible import find_possible, try_guess

def suggestion_optimal(words, possible, allowed, must_appear):
    lowest_total = 1000*1000
    best_guess = ''
    i = 0
    for guess in words:
        i = i + 1
        total_for_guess = 0

        # Imagine we guess a word, see how many options would remain on average
        for hidden_word in possible:            
            new_count = new_possible_count(possible, guess, hidden_word, set(hidden_word), allowed, must_appear)
            #print(f"hidden_word {hidden_word}, guess {guess} would give us {new_count} possible words left")
            total_for_guess = total_for_guess + new_count

        if total_for_guess < lowest_total:
            lowest_total = total_for_guess
            # The best guess is the one which eliminates the most words on average
            best_guess = guess
        #print(f"==== Average possibilities left for {guess} is {total_for_guess / len(possible)}")
        if i % 500 == 0:
            print(f"Looked at {i} words. Best so far is {best_guess} with {lowest_total / len(possible):.2f} remaining words on average.")
    return best_guess

def new_possible_count(possible, guess, hidden_word, hidden_word_set, allowed, must_appear):
    new_allowed = copy.deepcopy(allowed)
    new_must_appear = copy.deepcopy(must_appear)

    for i in range(len(guess)):
        g_char = guess[i]

        if g_char == hidden_word[i]:
            new_allowed[i] = { g_char }
        elif g_char in hidden_word_set:
             # The yellow character must appear in the word
            new_must_appear.add(g_char)
            # But the yellow character cannot be at that position
            if g_char in new_allowed[i]:
                new_allowed[i].remove(g_char)
        else:
            for j in range(len(guess)):
                if g_char in new_allowed[j]:
                    new_allowed[j].remove(g_char)

    count_possible = 0
    for w in possible:
        if is_possible_faster(w, new_allowed, new_must_appear):
            count_possible = count_possible + 1
    return count_possible
    #return len(find_possible(possible, new_allowed, new_must_appear))

def is_possible_faster(word, allowed, must_appear):
    for i in range(len(word)):
        if word[i] not in allowed[i]:
            return False
    for m in must_appear:
        if m not in word:
            return False
    return True    